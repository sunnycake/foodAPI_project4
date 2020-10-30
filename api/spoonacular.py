import requests
import os
from pprint import pprint

key = os.environ.get('SPOONACULAR_KEY')

url = 'https://api.spoonacular.com/recipes/complexSearch'

def get_recipe(search_recipe):
    try:
        query = {'query': search_recipe, 'addRecipeInformation': 'true','number': '1', 'apiKey': key}
        data = spoonacular_api_call(query)
        results = data['results']

        if results:
            result = results[0]
            recipe_name = result['title']
            recipe_url = result['spoonacularSourceUrl']
            recipe = recipe_name, recipe_url
            return recipe
        else:
            print('No results for recipe search. ')
            return None

    except Exception as e:
        print('Error with your query. ')


def spoonacular_api_call(query):
    return requests.get(url, params=query).json()