
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
    recipe_name, recipe_url = spoonacular.get_recipe(search_recipe)
    drink = nutritionix.get_drink(search_drink)
    image = handle_flickr_api_response(search_drink)

    print("\nHere's a recipe we think you might enjoy.\n")
    print(f'Recipe name: {recipe_name}')
    print(f'Recipe url: {recipe_url}')
    print(f'Drink: {drink}')
    print(f'Drink image: {image} \n')


    return recipe_name, recipe_url, drink, image 
  






