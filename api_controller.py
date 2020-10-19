from api import flickr, edamam, spoonacular
import random


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
result = getDrinkImage("mango lassi")
print(result)