from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://priem.volsu.ru/rating'
##response = requests.get(url, verify=False)
##bs = BeautifulSoup(response.text,"html.parser")
##print(bs)
##print(response)


options = webdriver.ChromeOptions()
options.add_argument("window-size=1200x600")
options.add_argument('ignore-certificate-errors')
options = Options()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) 
driver.get(url)




# select first dropdown
select = Select(driver.find_element(by=By.ID, value='level'))
select.select_by_visible_text('Бакалавриат')


# select second dropdown
from selenium.webdriver.common.action_chains import ActionChains as AC
span = driver.find_element(by=By.TAG_NAME, value='span')
span.click()
from selenium.webdriver.support.ui import WebDriverWait as wait

wait(driver, 10)
listSpecs = driver.find_element(by=By.CSS_SELECTOR, value='select#oop.form-control')
listSpecs.click()
wait(driver, 10)
# driver.execute_script("document.getElementById('oop').style.display = 'block'")
# listSpecs.find_element(by=By.XPATH, value="//select[@id='oop']//option[.='Программная инженерия']").click()
listSpecs.find_element(by=By.XPATH, value="./option[.='Программная инженерия']").click()


# from selenium.webdriver.support import expected_conditions as EC
# select = Select(driver.find_element(by=By.XPATH, value="//select[@id='oop']//option[text()='Программная инженерия']"))
# wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ))).click()





