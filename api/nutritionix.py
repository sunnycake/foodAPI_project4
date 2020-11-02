import requests 
import os
from pprint import pprint
#from caching import nutritionix_cache
import logging

# API key to open to see the API link 
app_key = os.environ.get('DRINK_KEY')
# API id to open to see the API link 
app_id = os.environ.get('DRINK_ID')

#API url 
url = 'https://api.nutritionix.com/v2/search'

#getting drink name from the API 
def get_drink(search_term):
    try:

        query = {'q': search_term,'limit': 1,'offset': 0,'appId': app_id,'appKey': app_key}
        data = nutritionix_api_call(query)
        results = data['results']
        # getting drink name and printing result, if not print drink not found, else error calling API 
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
    #API call 
    return requests.get(url, params=query).json()