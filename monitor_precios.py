import asyncio
import sys
import pickle
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from telegram import Bot

# --- 🚀 PARCHE PARA WINDOWS ---
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# --- 🔑 CONFIGURACIÓN DE TELEGRAM ---
TOKEN_TELEGRAM = "TU_TOKEN_AQUI"
CHAT_ID = "TU_ID_AQUI"


# --- 🥊 FUNCIÓN DE PUNTAJE ---
def calcular_puntaje_pro_v3(nombre, precio_usd):
    n = nombre.lower()
    p = 10 if "i7" in n else (7 if "i5" in n else 4)
    p += 8 if "16gb" in n else (12 if "32gb" in n else 4)
    detalles = ["pantalla mala", "reparar", "repuesto", "sin disco", "detalle", "quemado", "mica", "partido"]
    if any(d in n for d in detalles): p -= 30
    return round((p / precio_usd) * 100, 2) if precio_usd > 0 else 0


# --- 📲 FUNCIÓN DE ALERTA ---
async def enviar_alerta(modelo, precio, puntaje, enlace):
    try:
        bot = Bot(token=TOKEN_TELEGRAM)
        mensaje = (
            f"🚀 ¡GANGA DETECTADA, VICTOR ARMANDO!\n\n"
            f"💻 {modelo}\n"
            f"💰 Precio: {precio}$\n"
            f"🏆 Puntaje: {puntaje}\n\n"
            f"🔗 Link: {enlace}"
        )
        await bot.send_message(chat_id=CHAT_ID, text=mensaje)
        print(f"📲 Alerta enviada a tu Telegram por: {modelo[:20]}...")
    except Exception as e:
        print(f"❌ Error en Telegram: {e}")


# --- 1. EXTRACCIÓN ---
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
lista_laptops = []

try:
    driver.get("https://www.mercadolibre.com.ve")
    # Cargar cookies guardadas
    try:
        cookies = pickle.load(open("ml_cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()  # Refrescamos para que reconozca la sesión
        print("🍪 Cookies cargadas. ¡Entrando como Victor!")
    except:
        print("⚠️ No se encontraron cookies. Toca loguearse a mano.")
    print("\n--- 🛡️ MODO MANUAL ---")
    input("LOGUÉATE, RESUELVE EL CAPTCHA Y CUANDO ESTÉS ADENTRO DALE 'ENTER' AQUÍ: ")

    base_url = "https://listado.mercadolibre.com.ve/dell-latitude"

    for i in range(5):
        driver.get(f"{base_url}_Desde_{(i * 50) + 1}_NoIndex_True")
        print(f"🛰️ Escaneando Página {i + 1}...")
        time.sleep(5)

        cards = driver.find_elements(By.CLASS_NAME, "ui-search-result__wrapper")

        for item in cards:
            try:
                nombre = item.find_element(By.TAG_NAME, "h3").text
                p_raw = item.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text
                precio_usd = float(p_raw.replace('.', '').replace(',', '.'))
                enlace = item.find_element(By.TAG_NAME, "a").get_attribute("href")
                puntaje = calcular_puntaje_pro_v3(nombre, precio_usd)

                res = {"Modelo": nombre, "Precio $": precio_usd, "Puntaje": puntaje, "Enlace": enlace}
                lista_laptops.append(res)

                # 🔥 ALERTA EN TIEMPO REAL (Solo si es buena oferta)
                if puntaje > 8.0:
                    asyncio.run(enviar_alerta(nombre, precio_usd, puntaje, enlace))

            except:
                continue

finally:
    # --- 📊 2. EXCEL CON FORMATO IMPECABLE ---
    if lista_laptops:
        df = pd.DataFrame(lista_laptops).sort_values(by="Puntaje", ascending=False)
        nombre_archivo = "Monitor_Dell_UFC_FINAL_BOT_TELEGRAM.xlsx"

        with pd.ExcelWriter(nombre_archivo, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Ranking')
            workbook = writer.book
            worksheet = writer.sheets['Ranking']

            f_header = workbook.add_format(
                {'bold': True, 'bg_color': 'black', 'font_color': 'white', 'border': 1, 'align': 'center'})
            f_texto = workbook.add_format({'border': 1, 'valign': 'vcenter'})
            f_centrado = workbook.add_format({'border': 1, 'align': 'center', 'valign': 'vcenter'})

            for col_num, value in enumerate(df.columns.values):
                worksheet.write(0, col_num, value, f_header)

            for row_num in range(len(df)):
                worksheet.write(row_num + 1, 0, df.iloc[row_num, 0], f_texto)  # Modelo
                worksheet.write(row_num + 1, 1, df.iloc[row_num, 1], f_centrado)  # Precio $
                worksheet.write(row_num + 1, 2, df.iloc[row_num, 2], f_centrado)  # Puntaje
                worksheet.write(row_num + 1, 3, df.iloc[row_num, 3], f_texto)  # Enlace

            worksheet.set_column('A:A', 60)
            worksheet.set_column('B:C', 18)
            worksheet.set_column('D:D', 50)

        print(f"🏁 PROCESO TERMINADO. Revisa tu Excel y tu Telegram.")

    driver.quit()






















