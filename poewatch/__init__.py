import requests

from structures import Item
from utils import get_current_league

current_league = get_current_league()


def get_all_categories():
    url = "https://api.poe.watch/categories"
    my_headers = {'user-agent': 'currency-flipper/0.0.1'}
    response = requests.get(url, headers=my_headers)
    data = response.json()
    categories = [cat.get('name') for cat in data if cat.get('name')]
    return categories


def get_all_items():
    all_items = {}
    for category in get_all_categories():
        url = f"https://api.poe.watch/get?category={category}&league={current_league}"
        my_headers = {'user-agent': 'currency-flipper/0.0.1'}
        response = requests.get(url, headers=my_headers)
        try:
            error = eval(response.text).get('error')
        except Exception:
            error = ""
        if response.status_code == 200:
            data = response.json()
            if data:
                for item in data:
                    # Get ID
                    if 'id' in item:
                        item_id = str(item.get('id'))
                    else:
                        continue

                    # Get name
                    if 'name' in item:
                        item_name = item.get('name')
                    else:
                        continue

                    # Get price
                    if 'min' in item:
                        item_price = float(item.get('min'))
                    else:
                        continue

                    all_items[item_id] = Item(item_name, item_price)
        elif error == 'unknown category':
            continue
        else:
            raise ConnectionError(f'Could not get data from {url}.')
    return all_items


if __name__ == '__main__':
    all_items = get_all_items()
    print(all_items)
