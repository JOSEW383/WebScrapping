from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

CHANGE_SCREEN = False

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=options)

# Open chrome in other screen
if CHANGE_SCREEN:
    driver.set_window_position(2000,0)
    driver.maximize_window()
    time.sleep(1)

driver.get('https://mercadolibre.com.pe')
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input.nav-search-input'))).send_keys('teclado')
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.nav-icon-search'))).click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/aside/section/div[9]/ul/li[6]/a')))

url = driver.find_element_by_xpath('/html/body/main/div/div/aside/section/div[9]/ul/li[6]/a').get_attribute("href")
driver.get(url)

WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/main/div/div/section/ol')))
html_list = driver.find_element_by_css_selector('ol.ui-search-layout.ui-search-layout--stack') #Spaces must be replaced my full stop.
items = html_list.find_elements_by_tag_name("li")
for item in items:
    text = item.get_attribute("innerHTML")
    soup = BeautifulSoup(text, "html.parser")
    titulo = soup.find_all("h2")[0].string
    print(titulo)
    precio = soup.select("span.price-tag-fraction")[0].text
    print(precio)
    urls = soup.select("a.ui-search-item__group__element.ui-search-link")
    for url in urls:
        print(url.get("href"))
    print("-"*50)
    
driver.close()
