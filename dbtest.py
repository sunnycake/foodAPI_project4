import unittest
from database/food import db, logging


class TestRecordsDB(Food):
    test_db_url = 'test_food.db'

    

    # The name of this method is important - the test runner will look for it
    def setUp(self):
        database/food.db = self.test_db_url

        # drop everything from the DB to always start with an empty database/food
        with sqlite3.connect(self.test_db_url) as con:
            con.execute('DROP TABLE IF EXISTS records')
            
        con.close()

        with sqlite3.connect(self.test_db_url) as con:
            con.execute('CREATE TABLE IF NOT EXISTS records(recipe TEXT, url TEXT, drink TEXT, img JPG, bookmarked INTEGER)')
            
        con.close()

        self.db = database/food.db

    def test_add_new_food(self):
        recipe_name = 'Koshary'
        recipe_url = 'https://www.koshary.com'
        drink_name = 'Marinda'
        img_file_name = 'item.jpg'
       
        database/food.add_data(recipe_name, recipe_url, drink_name,img_file_name,)
        expected = {'Koshary', 'https://www.koshary.com', 'Marinda', 'item.jpg',}
        self.compare_db_to_expected(expected)    
    

    def test_food_already_in_data(self):
        recipe_name = 'Koshary'
        recipe_url = 'https://www.koshary.com'
        drink_name = 'Marinda'
        img_file_name = 'item.jpg'
       
        database/food.add_data(recipe_name, recipe_url, drink_name, img_file_name,)
        expected = {'Koshary', 'https://www.koshary.com', 'Marinda', 'item.jpg',}
        with self.assertRaises(er):
            #database/food.add_data(recipe_name, recipe_url, drink_name, img_file_name)
            self.compare_db_to_expected(expected)    

    def compare_db_to_expected(self, expected):
        conn = sqlite3.connect(self.test_db_url)
        all_data = conn.execute('SELECT * FROM records').fetchall()

      
        #self.assertEqual(len(expected.update()), len(all_data))

        for row in all_data:
            
            print(row)
            #self.assertIn(row[0], expected.update())
            #self.assertEqual(expected[row[0]], row[1])

        conn.close()

if __name__ == '__main__':
    unittest.main()
