import poeninja
import poewatch
from structures import Recipe
from utils import load_recipes, recipes_to_excel


def get_all_items():
    poewatch_items = poewatch.get_all_items()
    poeninja_items = poeninja.get_all_items()
    return poeninja_items | poewatch_items


all_items = get_all_items()


def calculate_cost_of_items(item_list):
    total_price = 0
    for item in item_list:
        item_id = item.get('url').rsplit('/', 1)[-1]
        total_price += all_items.get(item_id).price * item.get('count')
    return total_price


def calculate_number_of_trades(item_list):
    total_trades = 0
    for item in item_list:
        total_trades += item.get('count')
    return total_trades


recipes = load_recipes()
recipes = recipes.get('category')

all_recipes = {}
for category in recipes:
    all_recipes[category] = []
    for recipe_name in recipes.get(category):
        recipe_items = recipes.get(category).get(recipe_name)
        try:
            recipe_cost = calculate_cost_of_items(recipe_items.get('ingredients'))
            recipe_value = calculate_cost_of_items(recipe_items.get('outcomes'))
            recipe_total_trades = calculate_number_of_trades(recipe_items.get('ingredients'))
        except Exception as e:
            print(f"Skipped: {recipe_name}, reason: {e}")
            continue
        all_recipes[category].append(Recipe(recipe_name, recipe_cost, recipe_total_trades, recipe_value))

recipes_to_excel(all_recipes)
print('Done.')
