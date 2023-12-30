from scraper import Scraper

import logging


URL = "https://batdongsan.com.vn/cho-thue-nha-tro-phong-tro-quan-8/gia-tu-1-trieu-den-3-trieu?disIds=62,57"


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

    scraper = Scraper(URL)
    scraper.scrape()


if __name__ == '__main__':
    main()