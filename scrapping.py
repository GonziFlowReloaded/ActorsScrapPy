import requests
from bs4 import BeautifulSoup

URL = 'https://www.ryrcomputacion.com/tv-audio-y-video/auriculares/?orden=desc&marca=2458'

def ryr_precio():
#URL's to scrap
    
    #Get the page
    page = requests.get(URL)

    #Parse the page
    soup = BeautifulSoup(page.content, 'html.parser')

    #Get the products
    products_price = soup.find_all('h4', class_='mt-0 pecio_final ft')

    #Clean the products
    products_price = [price.get_text().replace('Precio especial',' ') for price in products_price]

    #Get the product name
    return products_price


def ryr_nombre():
    #Get the page
    page = requests.get(URL)

    #Parse the page
    soup = BeautifulSoup(page.content, 'html.parser')

    products_name = soup.find_all('h4', class_='card-title mb-1 h-40*')

    products_name = [name.get_text() for name in products_name]
    
    return products_name

