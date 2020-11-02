import requests
import os
from pprint import pprint
#from caching import spoonacular_cache
import logging

key = os.environ.get('SPOONACULAR_KEY')

url = 'https://api.spoonacular.com/recipes/complexSearch'

# function to get recipe from spoonacular api
def get_recipe(search_recipe):
    try: # try to search the api under these parameters
        query = {'query': search_recipe, 'addRecipeInformation': 'true','number': '1', 'apiKey': key}
        data = spoonacular_api_call(query)
        results = data['results']

        # find these elements in the results and return them. 
        if results:
            result = results[0]
            recipe_name = result['title']
            recipe_url = result['spoonacularSourceUrl']
            recipe = recipe_name, recipe_url
            return recipe
        else:
            print('No results for recipe search. ')

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    except Exception as e:
        logging.error(f'Error occured calling recipe API: {e}')
        return None, e

# Making the api request
def spoonacular_api_call(query):
    return requests.get(url, params=query).json()