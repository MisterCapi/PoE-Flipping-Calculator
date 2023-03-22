import time

import requests
from tqdm import tqdm

from poeninja.constants import links
from structures import Item


def get_all_items():
    all_items = {}
    for url in tqdm(links):
        my_headers = {'user-agent': 'currency-flipper/0.0.1'}
        response = requests.get(url, headers=my_headers)
        if response.status_code == 200:
            data = response.json()
            data = data.get('lines')
            for item in data:
                # Get ID
                if 'detailsId' in item:
                    item_id = item.get('detailsId')
                else:
                    continue

                # Get name
                if 'currencyTypeName' in item:
                    item_name = item.get('currencyTypeName')
                elif 'name' in item:
                    item_name = item.get('name')
                else:
                    continue

                # Get price
                if 'receive' in item and 'value' in item.get('receive'):
                    item_price = float(item.get('receive').get('value'))
                elif 'chaosValue' in item:
                    item_price = float(item.get('chaosValue'))
                else:
                    continue

                if item_id and item_name and item_price:
                    all_items[item_id] = Item(item_name, item_price)
        else:
            raise ConnectionError(f'Could not get data from {url}.')
        time.sleep(3)

    return all_items


if __name__ == '__main__':
    all_items = get_all_items()
    print(all_items)
