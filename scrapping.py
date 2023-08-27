import requests
from bs4 import BeautifulSoup



def ryr_precioYnombre_par():
    base_url = 'https://www.ryrcomputacion.com/tv-audio-y-video/auriculares/?page='
    all_products_price = []
    all_products_name = []

    for page_number in range(2, 10, 2):  # Recorrer páginas pares del 2 al 8 (ajusta según tus necesidades)
        url = base_url + str(page_number)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        products_name = soup.find_all('h4', class_='card-title mb-1 h-40*')
        products_name = [name.get_text() for name in products_name]

        products_price = soup.find_all('h4', class_='mt-0 pecio_final ft')
        products_price = [price.get_text().replace('Precio especial', ' ') for price in products_price]

        all_products_name.extend(products_name)
        all_products_price.extend(products_price)

    return all_products_price, all_products_name

def ryr_precioYnombre_inpar():
    base_url = 'https://www.ryrcomputacion.com/tv-audio-y-video/auriculares/?page='
    all_products_price = []
    all_products_name = []

    for page_number in range(1, 10, 2):  # Recorrer páginas impares del 1 al 9 (ajusta según tus necesidades)
        url = base_url + str(page_number)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        products_name = soup.find_all('h4', class_='card-title mb-1 h-40*')
        products_name = [name.get_text() for name in products_name]

        products_price = soup.find_all('h4', class_='mt-0 pecio_final ft')
        products_price = [price.get_text().replace('Precio especial', ' ') for price in products_price]

        all_products_name.extend(products_name)
        all_products_price.extend(products_price)

    return all_products_price, all_products_name

