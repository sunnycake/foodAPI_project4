import sqlite3
from peewee import *
#create reference to SQLite database file
db = SqliteDatabase("database/food.db")

"""represents a Food_recipe in the database
    """
class Food(Model):
    id = AutoField()
    food_name = CharField(unique=True)
    url = CharField()
    drink_name = CharField(unique=True)
    img_file_name = CharField(unique=True)

    class Meta():
        database = db #this model uses the "food.db" database
        constraints = [SQL('UNIQUE( food_name COLLATE NOCASE, drink_name COLLATE NOCASE )')]

    def __str__(self):
        return f'{self.id}: {self.food_name}: {self.url}: {self.drink_name}: {self.img_file_name}'

db.connect()
db.create_tables([Food])