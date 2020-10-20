import peewee
from model_food import Food
from model_drink import Drink

def check_if_recipe_exist(recipe_name):
    """checks if recipe exists. returns the primary ID, if it exists.
    and none value if it doesn't"""
    result = Food.get_or_none(Food.food_name == recipe_name)
    if result:
        return result.id

def create_food_record(food_name, url):
    """creates and returns a Model instance for the Food Model using the Field instances - food_name, url. """
    food = Food.create(food_name=food_name, url=url)
    return food


def create_drink_record(food, drink_name, ):
    """creates and returns a Model instance for the Drink Model
     using the Field instances - food, drink_name """
    drink = Drink.create(food=food, drink_name=drink_name)
    return drink
    
def display_food_with_drink():
    for row in Drink.select(Food.food_name, Drink.drink_name).join(Drink).dicts():
        print(row)
    


def delete_drink_by_id(primary_id):
    """get artwork by ID and deletes it and returns number of row deleted"""
    drink = Drink.get(Drink.id == primary_id)
    num_row_deleted = drink.delete_instance()
    return num_row_deleted

