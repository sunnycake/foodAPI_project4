FOOD RECIPE

The Food Recipe app is for food lovers to search for recipes. This application is developed to extract and display information about a food recipe, drink, along with a picture by asking of the drink. The program displays the data, then the user will have the option to either save or not save the output into the database. An output example would be (Food Name: Chicken 65 , Food Recipe Link: https://spoonacular.com/recipes/chicken-65-637876 , Drink Name: pepsi, Drink Picture: pepsi.jpg)


Requirements: Python, Peewee, Spoonacular, Nutritionix, Flickr, ID's and KEY's


Three different API's are being used in this application.

The 1st is Spoonacular, an recipe API that will be extracting recipe information about a specific food.

The 2nd is Nutritionix, a beverage API will be retriving drink information display.

The 3th is Flickr, a picture displayer, that will displaying the picture based in the drink input.

In order to run this application Peewee is needed, so you must have peewee since we're using it to connect with the database. (install using "pip install peewee")

This application won't work without API key's and/or id's, so for testing purposes we added them with code, user can set it up and test it. (PC: export KEY_NAME=13215464, THEN: echo $KEY_NAME. "repeat same process with ID's")

In order to see the pictures you need to download LigthShot

Example: (https://prnt.sc/v7fy6b) pinture(https://prnt.sc/v7gfp3)
Example: (https://prnt.sc/v7ghey) pinture(https://prnt.sc/v7ghpq)
