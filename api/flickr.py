import requests
import os
from pprint import pprint
from http import HTTPStatus

key = os.environ.get('FLICKR_KEY') 
url = 'https://www.flickr.com/services/rest/'

def get_image_data(drinkName):
    """Set up the parameters required in the search"""
    param = {
    'method' : 'flickr.photos.search',
    'text' : drinkName,
    'media': 'photos',
    'per_page' : 1,
    'sort' : 'relevance',
    'format': 'json',
    'nojsoncallback' : '1n',
    'api_key' : key
   }
    """return a value if connection is successfull or error if not"""
    try: 
        resonse = requests.get(url, params=param)
        data = resonse.json()
        results = data['photos']['photo']
        return results, None
    except Exception as error:
        return None, error

def extract_image_url_params(data):
    """get the query params from the data returned (get_image_data) function"""
    try:
        secret = data[0]['secret']
        photo_id = data[0]['id']
        server = data[0]['server']
        title = data[0]['title']
        return server, photo_id, secret, title
    except Exception as err:
        return err

def retrieve_image(server, photo_id, secret):
    try:
        fetchPhotoURL = f'https://live.staticflickr.com/{server}/{photo_id}_{secret}_m.jpg' #creates img
        photoResponse = requests.get(fetchPhotoURL)
        return photoResponse
    except Exception as err:
        return err

def create_img_file(title, image):
    try:
        filename = f'{title}.jpg'
        with open(filename, 'wb') as file:
            for image in image.iter_content():
                file.write(image)
            return filename
    except Exception as err:
        return err


def catch():
    pass
