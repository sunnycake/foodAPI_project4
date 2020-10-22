
from api import flickr, nutritionix, spoonacular
import random 

def get_food_info(search_recipe):
    search_recipe, recipe_url = spoonacular.get_recipe(search_recipe)
    print("\nHere's a recipe we think you might enjoy.\n")
    print(f'Recipe name: {search_recipe}')
    print(f'Recipe URL: {recipe_url}\n')

    return search_recipe, recipe_url

def get_drink_info(search_term):
    search_drink = nutritionix.get_drink(search_term)
    print('This is the drink you wanna to see. ')
    print(f'Drink Name: {search_drink}')
    return search_drink
  
  
def getDrinkImage(drinkName):
    img = flickr.getImage(drinkName)
    # error handler
    try:
        filename = f'{drinkName}.jpeg'

        with open(filename, 'wb') as f:
            for chunk in img.iter_content():
                f.write(chunk)

    except:
        print("error")
    return filename







