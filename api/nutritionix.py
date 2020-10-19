import requests
import os
from pprint import pprint
#Importing requests, os and pprints

# Application KEY to run program 
app_key = os.environ.get('DRINK_KEY')
#Aplication ID to run the program
app_id = os.environ.get('DRINK_ID')

# User will enter the drink they wanna search 
search_drink = 'COFFEE'

#URL that will pull the drink entered by user 
url = f'https://api.nutritionix.com/v2/search?q={search_drink}&limit=1&offset=0&appId={app_id}&appKey={app_key}'

#Requesting the drink info to display in the output 
data = requests.get(url).json()
pprint(data)
results = data['results']
for result in results:
    drink_name = result['item_name']
    

# Printing the name of drink requested by user     
print(f'Drink name: {drink_name}')
