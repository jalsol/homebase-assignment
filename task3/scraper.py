from bs4 import BeautifulSoup
from enum import IntEnum
from product_parser import ProductParser

import logging
import sqlite3
import time
import undetected_chromedriver as uc


CHROMIUM_EXECUTABLE_PATH = '/usr/bin/brave-browser-beta'
USER_DATA_DIR = '/home/jalsol/.config/BraveSoftware/Brave-Browser-Beta'
CLOUDFLARE_TIMEOUT = 5
CACHE_DURATION = 86400 # 1 day

class CacheDatabaseIndex(IntEnum):
    ID = 0
    ADDRESS = 1
    PRICE = 2
    PRICE_EXT = 3
    AREA = 4
    AREA_EXT = 5
    BEDROOMS_COUNT = 6
    DESCRIPTION = 7
    EXPIRED_DATE = 8


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
        self.db_conn = sqlite3.connect('data.sqlite')

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

            # product url has format: https://batdongsan.com.vn/<slug>-pr<product_id>
            # we need to extract the product id
            product_id = product_url.split('-')[-1] # get last element
            product_id = int(product_id[2:]) # remove 'pr' prefix

            cursor = self.db_conn.cursor()
            result = cursor.execute('SELECT * FROM cached_prop_info WHERE id = ?', (product_id,)).fetchone()

            if result is not None and result[CacheDatabaseIndex.EXPIRED_DATE] > time.time():
                logging.info(f'Product {product_id} is cached')
                continue

            self.driver.get(f'https://batdongsan.com.vn{product_url}')            
            product_parser = ProductParser(self.driver.page_source, product_id)
            product_parser.parse()

            self.db_conn.execute('INSERT OR REPLACE INTO cached_prop_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                 (product_id,
                                  product_parser.address,
                                  product_parser.price,
                                  product_parser.price_ext,
                                  product_parser.area,
                                  product_parser.area_ext,
                                  product_parser.bedrooms_count,
                                  product_parser.description,
                                  time.time() + CACHE_DURATION))
            self.db_conn.commit()

        self.driver.close()

