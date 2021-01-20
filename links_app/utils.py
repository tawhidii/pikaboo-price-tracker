import requests
from bs4 import BeautifulSoup
import lxml

def get_link_data(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    "Accept-Language" : "en",
    }
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    name = soup.select_one(selector='.page-title').getText().strip(',')
    price = soup.select_one(selector='.price').getText().replace(',','')
    price = float(price[1:])


    return name,price
