from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time 
import chromedriver_autoinstaller
import sys
chromedriver_autoinstaller.install()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("window-size=1200x600")
options.add_argument('ignore-certificate-errors')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options) 
driver.get("https://priem.volsu.ru/rating") 
driver.maximize_window()

webElement = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'level'))) 
select = Select(webElement).select_by_value('  Бакалавриат') 
 
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'select2-oop-container'))).click() 
 
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'select2-search__field'))).send_keys('Программная инженерия') 
 
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#select2-oop-results > li'))).click() 
 
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'form'))).send_keys('Очная') 

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'base'))).send_keys('бюджетная основа') 

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'search'))).click() 

table = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#rating_table'))) 

items = table.find_elements(By.XPATH, "//*[@class='yellow' or @class='default' or @class='in-order-first']")

from selenium.webdriver.common.action_chains import ActionChains 
action = ActionChains(driver) 
for item in items: 
    action.move_to_element(item).perform() 
    table = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.detail.found'))) 
    with open('filename.txt', 'a', encoding="utf-8") as f:
        f.write(table.get_attribute('innerHTML'))
        f.write('\n\n')
    print(table.get_attribute('innerHTML')) 

