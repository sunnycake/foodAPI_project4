from api import flickr, nutritionix, spoonacular
import random 
import logging
from pprint import pprint

def handle_flickr_api_response(drink_name):
    image_data, error = flickr.get_image_data(drink_name)
    if error:
        print(error)
    elif image_data:
        server, photo_id, secret, title = flickr.extract_image_url_params(image_data)
        img = flickr.retrieve_image(server, photo_id, secret)
        image_file = flickr.create_img_file(title, img)
        return image_file
    else:
        print("Sorry, couldn't find what you looking for. Please Try a different search ")

        
def get_food_info(search_recipe, search_drink):
    try:
        search_food = spoonacular.get_recipe(search_recipe)
        drink = nutritionix.get_drink(search_drink)
        img = handle_flickr_api_response(drink)
        recipe_name, recipe_url = search_food
        recipe = recipe_name, recipe_url, drink, img

        if recipe:
            print(f"\nHere's a recipe: {recipe}\n")
            return recipe
        else:
            print('Sorry, no recipe found.')
    except Exception as e:
        return None, e
