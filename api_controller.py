from api import flickr, nutritionix, spoonacular
import random 

def get_food_info(search_recipe, search_drink):
    try:
        search_food = spoonacular.get_recipe(search_recipe)
        drink = nutritionix.get_drink(search_drink)
        image = flickr.getImage(search_drink)
        
        recipe_name, recipe_url = search_food
        recipe = recipe_name, recipe_url, drink, image

        if recipe:
            print(f"\nHere's a recipe: {recipe}\n")
            return recipe
        else:
            print('Sorry, no recipe found.')
    except Exception as e:
        return None, e





