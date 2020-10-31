import requests
import os
from pprint import pprint
import logging

key = os.environ.get('FLICKR_KEY') 
url = 'https://www.flickr.com/services/rest'

def getImage(drinkName):
    try:
        query = {
            'method': 'flickr.photos.search','text': drinkName,'media': 'photos','per_page': 1,
            'sort': 'relevance','format': 'json','nojsoncallback': '1', 'api_key': key}
            
        data = flickr_api_call(query)
        results = data['photos']['photo']

        if results:
            result = results[0]
            secret = result['secret']
            photo_id = result['id']
            server = result['server']
            title = result['title']

            fetchPhotoURL = f'https://live.staticflickr.com/{server}/{photo_id}_{secret}_m.jpg' 
            photoResponse = requests.get(fetchPhotoURL)

            filename = f'{title}.jpg'
            with open(filename, 'wb') as file:
                for image in photoResponse.iter_content():
                    file.write(image)
                return filename
        else:
            print('No results for image search. ')
        
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    except Exception as e:
        logging.error(f'Error occured calling flickr API: {e}')
        return None, e


def flickr_api_call(query):
    return requests.get(url, params=query).json()
    