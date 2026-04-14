# 🛒 Mercado Libre Laptop Monitor & Value Ranker 🤖

[Read this in English](#english-version) | [Leer en Español](#versión-en-español)

---

## English Version

This automated system monitors **Mercado Libre** in real-time to detect the best deals on Dell Latitude laptops. It goes beyond simple scraping by implementing a custom ranking algorithm to identify high-value opportunities based on hardware specs.

### ✨ Key Features:
* **Custom "UFC" Ranking Logic:** A specialized algorithm that scores each laptop based on RAM, CPU generation, and physical condition vs. price.
* **Intelligent Web Scraping:** Built with **Selenium**, featuring session management (cookies) to optimize loading times and bypass security blocks.
* **Real-Time Telegram Alerts:** Integration with the **Telegram Bot API** to send instant notifications to your mobile device when a "Top Tier" deal is found.
* **Data Persistence & Export:** Stores findings and generates professional Excel reports using **Pandas** and **XlsxWriter**.

### 🚀 Tech Stack:
* **Python 3.x**
* **Selenium WebDriver**
* **Telegram API** (BotFather)
* **Pandas / XlsxWriter**

### 🛡️ Anti-Bot & Session Persistence
To avoid constant re-authentication and potential bot detection, use the `guardar_cookies.py` script:
1. Run `python guardar_cookies.py`.
2. Log in manually and solve any CAPTCHAs.
3. Once logged in, press **Enter** in the terminal to save your session.
4. Now, `monitor_precios.py` will automatically load these cookies for future runs.

---

## Versión en Español

Este sistema automatizado monitorea **Mercado Libre** en tiempo real para detectar las mejores ofertas en laptops Dell Latitude. El programa va más allá del scraping básico al implementar un algoritmo de ranking personalizado para identificar oportunidades de alto valor.

### ✨ Capacidades del Sistema:
* **Lógica de Ranking "UFC":** Algoritmo especializado que puntúa cada laptop basándose en memoria RAM, generación del procesador y estado físico frente al precio.
* **Web Scraping Inteligente:** Desarrollado con **Selenium**, incluye manejo de sesiones (cookies) para optimizar tiempos de carga y evitar bloqueos de seguridad.
* **Alertas de Telegram en Tiempo Real:** Integración con **Telegram Bot API** para enviar notificaciones instantáneas al celular cuando se detecta una oferta de "Nivel Pro".
* **Persistencia de Datos:** Almacena los hallazgos y genera reportes ejecutivos en Excel usando **Pandas** y **XlsxWriter**.

### 🚀 Tecnologías:
* **Python 3.x**
* **Selenium WebDriver**
* **Telegram API**
* **Pandas / XlsxWriter**

### 🛡️ Persistencia de Sesión y Anti-Bot
Para evitar re-autenticaciones constantes y detección de bot, utiliza el script `guardar_cookies.py`:
1. Ejecuta `python guardar_cookies.py`.
2. Inicia sesión manualmente y resuelve cualquier CAPTCHA.
3. Una vez dentro, presiona **Enter** en la terminal para guardar tu sesión.
4. Ahora, `monitor_precios.py` cargará automáticamente estas cookies en futuras ejecuciones.

---

### 📸 Execution & Output Preview / Vista Previa:

#### Bulk Console Output / Salida en Consola:

<img width="676" height="365" alt="image-telegram" src="https://github.com/user-attachments/assets/776aa297-3720-44c6-814e-a343a3f8062c" />

### Real-Time Telegram Alert / Alerta de Telegram:

<img width="453" height="569" alt="Telegram-bot" src="https://github.com/user-attachments/assets/15e9d1df-a05e-4e6c-9146-3372013d08f6" />


#### Final Report Result / Resultado Final del Reporte:
<img width="1366" height="736" alt="Excel-laptops" src="https://github.com/user-attachments/assets/c5a1c670-8bb6-4c09-b1d4-38c42105d556" />

---
Developed by / Desarrollado por **VICTOR ARMANDO DE OLIVEIRA RODRÍGUEZ**
