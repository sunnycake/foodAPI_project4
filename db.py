import peewee
from model_food import Food


def check_if_recipe_exist(recipe_name):
    """checks if recipe exists. returns the primary ID, if it exists.
    and none value if it doesn't"""
    result = Food.get_or_none(Food.recipe_name == recipe_name)
    if result:
        return result.id

def create_food_record(food_name, recipe_url, drink_name,img_file_name):
    """creates and returns a Model instance for the Food Model using the Field instances - food_name, url. """
    food = Food.create(food_name=food_name, recipe_url=recipe_url, drink_name=drink_name, img_file_name=img_file_name)
    return food

    
def display_recipe():
    for row in Food.select():
        print(row)

def delete_recipe_by_id(primary_id):
    """get artwork by ID and deletes it and returns number of row deleted"""
    recipe = Food.get(Food.id == primary_id)
    num_row_deleted = recipe.delete_instance()
    return num_row_deleted

