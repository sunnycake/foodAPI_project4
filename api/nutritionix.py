import requests
import os 
from pprint import pprint
import logging

key = os.environ.get('DRINK_KEY')
id = os.environ.get('DRINK_ID')

# https://api.nutritionix.com/v2/search?q=mango&limit=2&offset=0&appId=b3203af1&appKey=2b9b96bfe1278528cc9717ce7055a037

url = f'https://api.nutritionix.com/v2/search'

def get_drink(search_term):
    
    #setting up quiry and calling to API to pull information 
    try:
        query = {'q': search_term, 'limit': '1', 'offset': '0' , 'appId': id, 'appKey': key }
        data = nutritionix_api_call(query)
        results = data['results']
        
        # If name is found in the database will be displayed otherwise will pe=rint the error message
        if results:
            result = results [0]
            beverage = result['item_name']
            return beverage
        else:
            # Invalid name will diplay this message
            print('Sorry, Product not found in the database. Please Try Again.')
            return None

            
    except Exception as e:
        logging.exception(f'Error occured while calling the Nutritionix API. {e} ')
        
# api call 
def nutritionix_api_call(query):
    return requests.get(url, params=query).json()
