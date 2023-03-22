import pandas as pd
import requests
import yaml


def get_current_league():
    url = 'https://www.pathofexile.com/api/leagues'
    my_headers = {'user-agent': 'currency-flipper/0.0.1'}
    response = requests.get(url, headers=my_headers)
    if response.status_code == 200:
        data = response.json()
        for league in data:
            if league.get('endAt') is not None and not league.get('rules'):
                return league.get('id')
    return ""


def load_recipes():
    with open('recipes/recipes.yaml', "r") as stream:
        return yaml.safe_load(stream)


def recipes_to_excel(recipe_list_data):
    # Create a Pandas Excel writer using XlsxWriter as the engine
    writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')

    # Loop through each key in the dictionary and create a new sheet for it
    for sheet_name, recipe_list in recipe_list_data.items():
        # Create a DataFrame from the list of Recipes
        df = pd.DataFrame(recipe_list, columns=['name', 'cost', 'num_of_trades', 'value'])
        df['profit'] = df['value'] - df['cost']
        df['profit_per_trade'] = df['profit'] / df['num_of_trades']
        df['ROI %'] = 100 * (df['value'] / df['cost'] - 1)

        df = df.sort_values(by="profit_per_trade", ascending=False)

        # Write the DataFrame to the Excel sheet
        df.to_excel(writer, sheet_name=sheet_name, index=False)

        # Set the column width based on the longest value in each column
        worksheet = writer.sheets[sheet_name]

        # Apply filtering to the column
        worksheet.autofilter(0, 0, len(df.index), len(df.columns) - 1)

        for i, col in enumerate(df.columns):
            column_len = max(df[col].astype(str).map(len).max(), len(col))
            worksheet.set_column(i, i, column_len + 5)

            # Apply conditional formatting to the ROI column
            if col == 'ROI %' or col == 'profit_per_trade':
                # Define the color scale for the conditional formatting
                worksheet.conditional_format(1, i, len(df.index), i, {
                    'type': '3_color_scale',
                    'min_color': '#DD0000',
                    'mid_color': '#DDDD00',
                    'max_color': '#00DD00',
                    'min_type': 'num',
                    'max_type': 'num',
                    'min_value': -100,
                    'max_value': 100
                })

    # Save the Excel file
    writer.save()
