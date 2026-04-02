import pickle
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://www.mercadolibre.com.ve")
    print("\n--- 🍪 GENERADOR DE LLAVE ---")
    input("Loguéate, resuelve los desafíos y cuando estés en el Inicio, dale ENTER aquí...")

    # Guardamos las cookies en un archivo llamado 'ml_cookies.pkl'
    pickle.dump(driver.get_cookies(), open("ml_cookies.pkl", "wb"))
    print("✅ ¡Cookies guardadas con éxito! Ya puedes cerrar esto.")

finally:
    driver.quit()