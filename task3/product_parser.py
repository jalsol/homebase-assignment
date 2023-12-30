from bs4 import BeautifulSoup


LITERAL_TO_KEY = {
    'Mức giá': 'price',
    'Diện tích': 'area',
    'Phòng ngủ': 'bedrooms_count',
}


class ProductParser:
    def __init__(self, page_source, product_id = None):
        self.page_source = page_source
        self.soup = BeautifulSoup(self.page_source, 'html.parser')
        self.id = product_id
        self.address = None
        self.price = None
        self.price_ext = None
        self.area = None
        self.area_ext = None
        self.bedrooms_count = None
        self.description = None

    def _parse_product_id(self):
        if self.id is None:
            product_info = self.soup.find(class_='re__pr-info')
            self.id = product_info['prid']

    def _parse_address(self):
        address = self.soup.find(class_='js__pr-address')
        if address:
            self.address = address.text.strip()

    def _parse_short_info_items(self):
        short_info_items = self.soup.find_all(class_='js__pr-short-info-item')

        for item in short_info_items:
            item_title = item.find(class_='title').text.strip()
            item_value = item.find(class_='value').text.strip()
            item_ext = item.find(class_='ext')
            key = LITERAL_TO_KEY.get(item_title, item_title)

            if item_value.endswith(' PN') and key == 'bedrooms_count':
                item_value = item_value[:-3]

            setattr(self, key, item_value)
            if item_ext:
                setattr(self, f'{key}_ext', item_ext.text.strip())

    def _parse_description(self):
        description = self.soup.find(class_='re__section-body')
        self.description = description.text.strip() if description else ''

    def parse(self):
        self._parse_product_id()
        self._parse_address()
        self._parse_short_info_items()
        self._parse_description()