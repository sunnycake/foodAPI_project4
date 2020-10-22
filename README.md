 FOOD PROJECT


Food recipe, Drink, and Image API 

Three API's are being used for this application: 

The first API is Spoonocular, which will be pulling the Food name, along with a link for more information about the recipe.

The second API is Nutrientix, that will be pulling the Drink name, and the last API is Flickr, that will be displaying the picture based on the user drink input.

In order to run this application Peewee is needed, so you have to have peewee since we're using it to connect with the database. (install using "pip install peewee")

This application won't work without API key's and/or id's, so for testing purposes we added them with code, user can set it up and test it.      (PC: export KEY_NAME=13215464, THEN: echo $KEY_NAME. "repeat same process with ID's") 

Then user will be able to run the application to enter the recipe name, and drink name, application will talk to the API's to pull the information for user.

An output Example would be:      

                            Food Name:  Chicken 65, Link: (recipe link for more information), Drink Name:  Pepsi, Picture: (Photo displayed)





