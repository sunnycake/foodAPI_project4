import sqlite3
from peewee import *
from model_food import Food


#create reference to SQLite database file
db = SqliteDatabase("database/food.db")

"""represtents a drink in the database
    """
class Drinks(Model):
    id = AutoField()
    food = ForeignKeyField(Food, backref='food')
    drink_name = CharField(unique=True)
    

    class Meta():
        database = db #this model uses the "food.db" database
        constraints = [SQL('UNIQUE( drink_name COLLATE NOCASE )')]

    def __str__(self):
        return f'{self.id}: Food: {self.food}: {self.drink_name}' 
db.connect()
db.create_tables([Drinks]) 