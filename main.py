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
                print('Good bye!')
                break
            else:
                print('\nNot a valid choice.\n')
        except ValueError as e:
            print('\nPlease enter a numeric choice.\n')


def display_menu(): # Menu option for user
    print('1: Search recipe')
    print('2: Delete a recipe')
    print('3: Display all recipes')
    print('4: Exit')


def search_recipe():
    search_recipe = ui.get_search_term() 
    recipe_name, recipe_url = api_controller.get_food_info(search_recipe)

    save = input('Do you want to save this recipe? Enter "y" or "n": ')

    if save == 'y':
        db.save_recipe(recipe_name, recipe_url)
    elif save == 'n':
        print('Good bye! ')

    
def delete_recipe():
    pass


def display_all_recipes():
    print("\nHere's all your recipes: \n")
    all_recipes = db.show_all_recipes()


if __name__ == "__main__":
    main()
