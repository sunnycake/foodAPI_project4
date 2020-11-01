import requests
import os
import json
from pprint import pprint
from http import HTTPStatus

key = os.environ.get('FLICKR_KEY') 
url = 'https://www.flickr.com/services/rest'

errors = {
    "msg": str
}
    
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

    try: 
        resonse = requests.get(url, params=param)
        data = resonse.json()
        results = data['photos']['photo']
        return results, None
    except requests.exceptions.ConnectionError:
        errors['msg'] = 'OOPS! Connection Error'
        return None, errors
    except requests.exceptions.HTTPError:
        errors['msg'] = 'Sorry! Page Not Found. Please Check the URL'
        return None, errors
    except KeyError:
        errors['msg'] = 'OOPS! Key ERROR. Please Check Query Params'
        return None, errors
    except json.JSONDecodeError:
        errors['msg'] = 'OOPS! Please check the url path'
        return None, errors
    except requests.RequestException:
        errors['msg'] = 'All we know is an error happened!'
        return None, errors

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
        save_path = '../images'
        filename = f'{title}.jpg'
        complete_file_name = os.path.join(save_path, filename)
        with open(complete_file_name, 'wb') as file:
            for image in image.iter_content():
                file.write(image)
            return filename
    except Exception as err:
        return err



