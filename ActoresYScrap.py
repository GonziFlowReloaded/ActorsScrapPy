import requests
from bs4 import BeautifulSoup
import pykka

class ScraperActor(pykka.ThreadingActor):
    def __init__(self, actor_number):
        super().__init__()
        self.actor_number = actor_number
        print(f"Actor {self.actor_number} created.")

    def scrape_ryr_auris(self):
        URL = 'https://www.ryrcomputacion.com/tv-audio-y-video/auriculares/?orden=desc&marca=2458'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        products_price = soup.find_all('h4', class_='mt-0 pecio_final ft')
        products_name = soup.find_all('h4', class_='card-title mb-1 h-40*')
        
        products_price = [price.get_text().replace('Precio especial', ' ') for price in products_price]
        products_name = [name.get_text() for name in products_name]
        
        result = []
        for i in range(len(products_name)):
            item = products_name[i] + ' Precio: ' + products_price[i]
            result.append(item)

        print(f"Actor {self.actor_number}: Scraped {len(result)} products")
        return result


if __name__ == '__main__':
    scraper_actor1 = ScraperActor.start(actor_number=1)
    scraper_actor2 = ScraperActor.start(actor_number=2)

    def print_result(result):
        for item in result:
            print(item)

    future1 = scraper_actor1.proxy().scrape_ryr_auris()
    future2 = scraper_actor2.proxy().scrape_ryr_auris()

    future1.get().map(print_result)
    future2.get().map(print_result)