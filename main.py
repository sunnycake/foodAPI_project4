import peewee
import ui
from api import spoonacular, nutritionix, flickr
import api_controller
import db


def main():
    while True:
        try:
            display_menu()
            choice = int(input('Enter choice: '))
            if choice == 1:
                search_recipe()
            elif choice == 2:
                delete_recipe()
            elif choice == 3:
                display_all_recipes()
            elif choice == 4:
                ui.message('Good bye!')
                break
            else:
               ui.message('\nNot a valid choice.\n')
        except ValueError as e:
            ui.message('\nPlease enter a numeric choice.\n')


def display_menu(): # Menu option for user
    print('1: Search recipe')
    print('2: Delete a recipe')
    print('3: Display all recipes')
    print('5: Exit')


def search_recipe():
    """get info about the user's choose food and drink from 3 different api.
        """
    search_recipe = ui.get_non_empty_string("Please Enter recipe name? ") 
    search_drink = ui.get_non_empty_string("Please enter drink name? ")
    drink_name = api_controller.get_drink_info(search_drink)
    drink_img = flickr.getImage(search_drink)
    img_file_name = api_controller.getDrinkImage(drink_img)
    recipe_name, recipe_url = api_controller.get_food_info(search_recipe)
    save = ui.save_or_not_save()
    if save:
        save_record(recipe_name, recipe_url, drink_name, img_file_name)
    ui.message("Good Bye!")

def save_record(recipe_name, recipe_url, drink_name, img_file_name):
    """saves a recipe record in to the database and handles for duplicate data entry"""
    try:
        food_record = db.create_food_record(recipe_name, recipe_url, drink_name, img_file_name)
        food_record.save()
    except peewee.IntegrityError:
        ui.message(f"Failed to add! Either the Name: {recipe_name}, or the Drink: {drink_name} already exist in the database ")


def delete_recipe():
    get_id = ui.get_id()
    try:
        rows_deleted = db.delete_recipe_by_id(get_id)
        ui.message(f"successfully deleted {rows_deleted} row")
    except peewee.DoesNotExist:
        ui.message("The record you are trying to delete doesn't exist")


def display_all_recipes():
    ui.message("\nHere's all your recipes: \n")
    db.display_recipe()
    pass

if __name__ == "__main__":
    main()
