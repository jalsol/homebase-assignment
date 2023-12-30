from bs4 import BeautifulSoup
from product_parser import ProductParser

import logging
import undetected_chromedriver as uc
import time


CHROMIUM_EXECUTABLE_PATH = '/usr/bin/brave-browser'
USER_DATA_DIR = '/home/jalsol/.config/BraveSoftware/Brave-Browser'
CLOUDFLARE_TIMEOUT = 5


class Scraper:
    def __init__(self, url: str):
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

    def _load_url(self):
        logging.info('Loading URL...')

        self.driver.get(self.url)
        time.sleep(CLOUDFLARE_TIMEOUT)

        self.page_source = self.driver.page_source
        self.cookies = self.driver.get_cookies()
        logging.debug(f'Cookies: {self.cookies}')

        self.driver.close()

    def scrape(self):
        self._load_url()

        soup = BeautifulSoup(self.page_source, 'html.parser')
        products = soup.find_all(class_='js__product-link-for-product-id')

        for product in products:
            product_url = product['href']
            logging.debug(f'Product URL: {product_url}')
