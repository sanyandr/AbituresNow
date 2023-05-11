from bs4 import BeautifulSoup as soup
import requests

url = 'https://priem.volsu.ru/rating'
response = requests.get(url, verify=False)
bs = soup(response.text,"html.parser")
page = bs.head.title
print(page)
