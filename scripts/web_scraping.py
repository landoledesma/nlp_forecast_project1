import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from urllib.parse import urljoin

# Configurar opciones de Firefox
firefox_options = Options()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')

# Ruta al geckodriver
geckodriver_path = "/usr/local/bin/geckodriver"

# Iniciar el navegador con Selenium
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service, options=firefox_options)

base_url = "https://www.cityobservatory.birmingham.gov.uk/@birmingham-city-council/purchase-card-transactions"
driver.get(base_url)

# Crear directorio de datos si no existe
if not os.path.exists('data'):
    os.makedirs('data')

# Función para descargar archivos XLS
def download_xls_files(soup, base_url):
    xls_links = soup.find_all('a', href=True)
    for link in xls_links:
        if link['href'].endswith('.xls'):
            xls_url = urljoin(base_url, link['href'])  # Construir URL absoluta
            xls_filename = os.path.join('data', xls_url.split('/')[-1])
            try:
                xls_response = requests.get(xls_url)
                xls_response.raise_for_status()  # Verifica si la solicitud fue exitosa
                with open(xls_filename, 'wb') as f:
                    f.write(xls_response.content)
                print(f"Downloaded: {xls_filename}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to download {xls_url}: {e}")

# Descargar archivos en la página inicial
response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')
download_xls_files(soup, base_url)

# Función para cargar más páginas
def load_more_pages():
    while True:
        try:
            # Verificar si el botón "Cargar más" está presente
            load_more_button = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//button[@class='ml-6 null']"))
            )

            # Verificar si el botón es clicable
            if load_more_button.is_enabled():
                load_more_button.click()
                time.sleep(5)  # Esperar a que se carguen los nuevos archivos

                # Descargar nuevos archivos XLS
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                download_xls_files(soup, base_url)
            else:
                print("No more pages to load or the button is disabled.")
                break
        except Exception as e:
            print("No more pages or an error occurred:", e)
            break

# Cargar más páginas y descargar archivos
load_more_pages()

driver.quit()
