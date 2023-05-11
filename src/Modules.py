from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://priem.volsu.ru/rating'


from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("window-size=1200x600")
options.add_argument('ignore-certificate-errors')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) 
driver.get(url)



# # select first dropdown
# # select = Select(driver.find_element(by=By.ID, value='level'))
# # select.select_by_visible_text('Бакалавриат')

# driver.execute_script("$('#level').val('  Бакалавриат').trigger('change')")
# driver.execute_script("$('#oop').select2('open');")

# driver.implicitly_wait(300)

# select = Select(driver.find_element(by=By.ID, value='oop'))
# select.select_by_value('000002948')

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# wait = WebDriverWait(20)
# pri = wait.until(EC.element_to_be_clickable(By.XPATH, "//*[@id='oop']/option[28]")).click()


from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import Select 
import time 
 

 
driver.get("https://priem.volsu.ru/rating") 
 
webElement = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'level'))) 
select = Select(webElement).select_by_value('  Бакалавриат') 
 
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'select2-oop-container'))).click() 
 
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'select2-search__field'))).send_keys('Программная инженерия') 
 
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#select2-oop-results > li'))).click() 
 
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'form'))).send_keys('Очная') 

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'base'))).send_keys('бюджетная основа') 

searchBtn = Select(driver.find_element(by=By.ID, value='search').click())