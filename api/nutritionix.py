import requests 
import os
from pprint import pprint

app_key = os.environ.get('DRINK_KEY')
app_id = os.environ.get('DRINK_ID')


def get_drink(search_term):
    
    url = f'https://api.nutritionix.com/v2/search?q={search_term}&limit=1&offset=0&appId={app_id}&appKey={app_key}'
    try:
        data = requests.get(url).json()
        results = data['results']

        for result in results:
            drink_name = result['item_name']
        return drink_name

    except:
        print('Error with your query. ')