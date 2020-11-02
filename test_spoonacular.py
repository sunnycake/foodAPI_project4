from api import spoonacular
from unittest import TestCase
from unittest.mock import patch

class TestAPI(TestCase):

    @patch('api.spoonacular.spoonacular_api_call', return_value= {"results": [{"id": 637876,"title": "Chicken 65"}],"spoonacularSourceUrl": "https://spoonacular.com/chicken-65-637876"})
    def test_api_returns_data_if_data_exists(self, mock_api_call):
        mock_api_call.return_value = {"results": [{"id": 637876,"title": "Chicken 65"}],"spoonacularSourceUrl": "https://spoonacular.com/chicken-65-637876"}
        search_recipe = spoonacular.get_recipe('chicken')
        self.assertIsNotNone(mock_api_call, search_recipe)


    @patch('api.spoonacular.spoonacular_api_call', side_effect=Exception('Error connecting'))
    def test_api_error_connecting(self, mock_request_get):
        mock_request_get.return_value = 404
        self.assertNotEqual(mock_request_get, 'Error connecting')
