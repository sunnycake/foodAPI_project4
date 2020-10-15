from api import flickr, edamam, spoonacular
import random 


def get_food_info(search_food, search_drink):
    
    what_to_search_for_image = random.choice([search_food, search_drink])
    image = flickr.get_image(what_to_search_for_image)


    drink = edamam.get_drink(search_drink)
    recipe = spoonacular.get_recipe(search_food)

    return image, drink, recipe



