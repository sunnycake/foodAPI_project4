
from api import flickr, nutritionix, spoonacular
import random 

def get_food_info(search_recipe, search_drink):
    recipe_name, recipe_url = spoonacular.get_recipe(search_recipe)
    drink = nutritionix.get_drink(search_drink)
    image = flickr.getImage(search_drink)

    print("\nHere's a recipe we think you might enjoy.\n")
    print(f'Recipe name: {recipe_name}')
    print(f'Recipe url: {recipe_url}')
    print(f'Drink: {drink}')
    print(f'Drink image: {image} \n')


    return recipe_name, recipe_url, drink, image 
  






