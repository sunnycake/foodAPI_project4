
from api import flickr, nutritionix, spoonacular
import random 

def get_food_info(search_recipe):
    search_recipe, recipe_url = spoonacular.get_recipe(search_recipe)
    drink = nutritionix.get_drink(search_drink)
    image = flickr.getImage(search_drink)

    print("\nHere's a recipe we think you might enjoy.\n")
    print(f'Recipe name: {search_recipe}')
    print(f'Recipe url: {recipe_url}')
    print(f'Drink: {drink}')
    print(f'Drink image: {image} \n')


    return search_recipe, recipe_url, drink, image 
  






