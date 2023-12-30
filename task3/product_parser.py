from bs4 import BeautifulSoup


LITERAL_TO_KEY = {
    'Mức giá': 'price',
    'Diện tích': 'area',
    'Phòng ngủ': 'bedrooms_count',
}


class ProductParser:
    def __init__(self, page_source):
        self.page_source = page_source
        self.soup = BeautifulSoup(self.page_source, 'html.parser')
        self.data = {}

    def _parse_product_id(self):
        product_info = self.soup.find(class_='re__pr-info')
        self.data['id'] = product_info['prid']

    def _parse_address(self):
        address = self.soup.find(class_='js__pr-address')
        if address:
            self.data['address'] = address.text.strip()

    def _parse_short_info_items(self):
        short_info_items = self.soup.find_all(class_='js__pr-short-info-item')

        for item in short_info_items:
            item_title = item.find(class_='title').text.strip()
            item_value = item.find(class_='value').text.strip()
            item_ext = item.find(class_='ext')
            key = LITERAL_TO_KEY.get(item_title, item_title)

            if item_ext:
                item_ext = item_ext.text.strip()
                self.data[key] = { 'value': item_value, 'ext': item_ext }
            else:
                self.data[key] = { 'value': item_value }

    def _parse_description(self):
        description = self.soup.find(class_='re__section-body')
        self.data['description'] = description.text if description else ''

    def parse(self):
        self._parse_product_id()
        self._parse_address()
        self._parse_short_info_items()
        self._parse_description()