import api_controller
import db

# todo menu - search or show bookmarks 
food = input('enter food')
drink = input('enter drink')

image, recipe, drink = api_controller.get_food_info(food, drink)

print(recipe)
print(drink)
image.show()

save = input('do you want to save this?')

if save == 'y':
    db.save(recipe, drink, image)  # save the image filename 


# todo show saved results 