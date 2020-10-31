import requests
import os
from pprint import pprint
from caching import spoonacular_cache

# KEY d688a6a66b854751b47ff02fa3e115d1 for testing purposes. 

key = os.environ.get('SPOONACULAR_KEY')

url = 'https://api.spoonacular.com/recipes/complexSearch'

def get_recipe(search_recipe):
    try:
        query = {'query': search_recipe, 'addRecipeInformation': 'true','number': '1', 'apiKey': key}
        data = requests.get(url, params=query).json()
        results = data['results']

        for result in results:
            title = result['title']
            recipe_url = result['spoonacularSourceUrl']

        return title, recipe_url


    except Exception as e:
        print('Error with your query. ')