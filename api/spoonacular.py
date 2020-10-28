import requests
import os
from pprint import pprint
import logging

key = os.environ.get('SPOONACULAR_KEY')

url = 'https://api.spoonacular.com/recipes/complexSearch'

def get_recipe(search_recipe):
    try:
        query = {'query': search_recipe, 'addRecipeInformation': 'true','number': '1', 'apiKey': key}
        data = spoonacular_api_call(query)
        results = data['results']

        if results:
            result = results[0]
            title = result['title']
            recipe_url = result['spoonacularSourceUrl']
            return title, recipe_url
        else:
            print('Sorry, could not get a recipe.')
    except Exception as e:
        logging.exception(f'Error occured while calling the API. {e}')


def spoonacular_api_call(query):
    return requests.get(url, params=query).json()
