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

# Configure Firefox options
firefox_options = Options()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')

# Path to geckodriver
geckodriver_path = "/usr/local/bin/geckodriver"

# Start the browser with Selenium
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service, options=firefox_options)

base_url = "https://www.cityobservatory.birmingham.gov.uk/@birmingham-city-council/purchase-card-transactions"
driver.get(base_url)

# Create data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Function to download XLS files
def download_xls_files(soup, base_url):
    xls_links = soup.find_all('a', href=True)
    for link in xls_links:
        if link['href'].endswith('.xls'):
            xls_url = urljoin(base_url, link['href'])  # Build absolute URL
            xls_filename = os.path.join('data', xls_url.split('/')[-1])
            try:
                xls_response = requests.get(xls_url)
                xls_response.raise_for_status()  # Check if the request was successful
                with open(xls_filename, 'wb') as f:
                    f.write(xls_response.content)
                print(f"Downloaded: {xls_filename}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to download {xls_url}: {e}")

# Download files on the initial page
response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')
download_xls_files(soup, base_url)

# Function to load more pages
def load_more_pages():
    while True:
        try:
            # Check if the "Load more" button is present
            load_more_button = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//button[@class='ml-6 null']"))
            )

            # Check if the button is clickable
            if load_more_button.is_enabled():
                load_more_button.click()
                time.sleep(5)  # Wait for new files to load

                # Download new XLS files
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                download_xls_files(soup, base_url)
            else:
                print("No more pages to load or the button is disabled.")
                break
        except Exception as e:
            print("No more pages or an error occurred:", e)
            break

# Load more pages and download files
load_more_pages()

driver.quit()
