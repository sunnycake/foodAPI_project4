import requests
import os
from pprint import pprint

# KEY d688a6a66b854751b47ff02fa3e115d1 for testing purposes. 

key = os.environ.get('SPOONACULAR_KEY')

url = 'https://api.spoonacular.com/recipes/complexSearch'

def get_recipe(search_recipe):
    try:
        query = {'query': search_recipe, 'addRecipeInformation': 'true','number': '1', 'apiKey': key}
        
        data = spoonacular_api_call(query)
        
        results = data['results']

        # for result in results:
        #     title = result['title']
        #     recipe_url = result['spoonacularSourceUrl']

        if results: # is list at least 1 thing long
            result = results[0]   # get first thing
            title = result['title']
            recipe_url = result['spoonacularSourceUrl']
            return title, recipe_url

        else:
            # handle no results 
            pass  # todo 


    except Exception as e:   # todo improve error handling. 
        # you have no idea what is wrong here. a syntax error, error with API, error with key
        # no results, URL has typo, API server down ???? 
        # import logging and log the exception 
        print('Error with your query. ')  # no user message here. use logging, for example log the e exception variable 

    # todo the function needs to return data, if data is available
    # todo think about how it can communicate that there was a successful request but no recipes found
    # todo think about how it can communicate the request was not successful - server down, not internet, key error...


# mocking this is going to be easier than mocking request.get 
def spoonacular_api_call(query):
    # you can handle errors in get_recipie
    return requests.get(url, params=query).json()
        