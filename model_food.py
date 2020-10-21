import sqlite3
from peewee import *
#create reference to SQLite database file
db = SqliteDatabase("database/food.db")

"""represents a Food_recipe in the database
    """
class Food(Model):
    id = AutoField()
    recipe_name = CharField(unique=True)
    recipe_url = CharField()
    drink_name = CharField(unique=True)
    img_file_name = CharField(unique=True)

    class Meta():
        database = db #this model uses the "food.db" database
        constraints = [SQL('UNIQUE( recipe_name COLLATE NOCASE, drink_name COLLATE NOCASE )')]

    def __str__(self):
        return f'{self.id}: {self.recipe_name}: {self.recipe_url}: {self.drink_name}: {self.img_file_name}'

db.connect()
db.create_tables([Food])