import requests
import os
from pprint import pprint
from caching import flickr_cache

key = os.environ.get('FLICKR_KEY') # 4dd2de713ae2dfae3dc724620b1c8b92 

def getImage(drinkName):

    url = f'https://www.flickr.com/services/rest/?method=flickr.photos.search&text={drinkName}&media=photos&per_page=1&sort=relevance&format=json&nojsoncallback=1&api_key={key}'
    try:
        data = requests.get(url)
        jsonFlickrApi = data.json()
        results = jsonFlickrApi['photos']['photo']
        for result in results:
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

    except Exception as e:
        print('Error with your query. ')
    