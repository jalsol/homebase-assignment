from bs4 import BeautifulSoup
from product_parser import ProductParser

import json
import logging
import time
import undetected_chromedriver as uc


CHROMIUM_EXECUTABLE_PATH = '/usr/bin/brave-browser-beta'
USER_DATA_DIR = '/home/jalsol/.config/BraveSoftware/Brave-Browser-Beta'
CLOUDFLARE_TIMEOUT = 5


class Scraper:
    def __init__(self, url: str, output_file: str = 'data.json'):
        logging.info('Scraper initialized')
        logging.info(f'Chromium path: {CHROMIUM_EXECUTABLE_PATH}')
        logging.info(f'User data dir: {USER_DATA_DIR}')
        logging.debug(f'URL: {url}')
        self.url = url
        self.cookies = None
        self.page_source = None
        self.driver = uc.Chrome(use_subprocess=True,
                                browser_executable_path=CHROMIUM_EXECUTABLE_PATH,
                                user_data_dir=USER_DATA_DIR)
        self.data = []

    def _set_cookies(self, cookies):
        self.cookies = cookies
        logging.debug(f'Cookies: {self.cookies}')
        for cookie in self.cookies:
            self.driver.add_cookie(cookie)

    def _load_url(self):
        logging.info('Loading URL...')
        self.driver.get(self.url)

        if self.cookies is None:
            time.sleep(CLOUDFLARE_TIMEOUT)
            self._set_cookies(self.driver.get_cookies())

        self.page_source = self.driver.page_source

    def scrape(self):
        self._load_url()

        soup = BeautifulSoup(self.page_source, 'html.parser')
        products = soup.find_all(class_='js__product-link-for-product-id')

        for product in products:
            product_url = product['href']
            logging.debug(f'Product URL: {product_url}')

            self.driver.get(f'https://batdongsan.com.vn{product_url}')            
            product_parser = ProductParser(self.driver.page_source)
            product_parser.parse()
            self.data.append(product_parser.data)
        
        with open('data.json', 'w') as out_file:
            json.dump(self.data, out_file, indent=2, ensure_ascii=False)

        self.driver.close()

