import pickle
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# --- ⚙️ BROWSER SETUP / CONFIGURACIÓN DEL NAVEGADOR ---
# Initializes the webdriver to handle manual login and session capture.
# Inicializa el webdriver para gestionar el inicio de sesión manual y la captura de sesión.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Navigate to Mercado Libre to initiate session / Navegar a Mercado Libre para iniciar sesión
    driver.get("https://www.mercadolibre.com.ve")
    
    print("\n--- 🍪 SESSION COOKIE GENERATOR / GENERADOR DE LLAVE DE SESIÓN ---")
    input("Loguéate, resuelve los desafíos y cuando estés en el Inicio, dale ENTER aquí...")

    # --- 💾 COOKIE PERSISTENCE / PERSISTENCIA DE COOKIES ---
    # Captures current browser cookies and saves them to a file for later reuse.
    # Captura las cookies actuales del navegador y las guarda en un archivo para reutilizarlas después.
    pickle.dump(driver.get_cookies(), open("ml_cookies.pkl", "wb"))
    
    print("✅ ¡Cookies guardadas con éxito! Ya puedes cerrar esto.")

finally:
    # --- 🔒 CLEANUP / LIMPIEZA ---
    # Closes the browser to free system resources.
    # Cierra el navegador para liberar recursos del sistema.
    driver.quit()
