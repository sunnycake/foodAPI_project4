import requests 
import os
from pprint import pprint
import logging

app_key = os.environ.get('DRINK_KEY')
app_id = os.environ.get('DRINK_ID')

url = 'https://api.nutritionix.com/v2/search'

def get_drink(search_term):
    try:
        query = {'q': search_term,'limit': 1,'offset': 0,'appId': app_id,'appKey': app_key}
        data = nutritionix_api_call(query)
        results = data['results']

        if results:
            result = results[0]
            beverage = result['item_name']
            return beverage
        else:
            print('No results for drink search. ')

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    except Exception as e:
        logging.error(f'Error occured calling drink API: {e}')
        return None, e


def nutritionix_api_call(query):
    return requests.get(url, params=query).json()