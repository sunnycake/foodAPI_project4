from api import spoonacular
from unittest import TestCase
from unittest.mock import patch

class TestAPI(TestCase):

    # option 1 - happy path - at least one recipe returned 
    # mock the API call
    @patch('api.spoonacular.spoonacular_api_call', return_value={'results': ['name', 'cheese']})  # replace with example response in the same structure the API uses
    def test_api_returns_data_if_data_exists(self, mock_api_call):
        # if it's easier you can set the side effect here instead of in the @patch decorator
        mock_api_call.return_value = [ 'replace with json' ]  # whatever it is 
        title, url = spoonacular.get_recipe('example food')
        # assert title is the title from the example response data
        # assert url is the url from the example response 

    # option 2 - ok path - no data - searching for something like "235645630349u90354u39045u" that there are no recipes for 
    # results is empty list  
    # change the method name :)
    @patch('api.spoonacular.spoonacular_api_call', return_value='')  # fill in example no data response in the same format the API uses
    def test_api_does_whatever_it_does_when_no_results(self, mock_api_call):
        recipe = spoonacular.get_recipe('not a food')
        # assert that the get_recipe method correctly returns a response that indicates no value 


    # option 3 - unhappy path - call is made, response recived but it is an error message 
    # # many APIs return a JSON response e.g. { "error": "missing API key" }
    # what if JSON is not in expected format? 
    @patch('api.spoonacular.spoonacular_api_call', return_value='')  # fill in example no error JSON data response in the same format the API uses
    def test_api_call_handles_error_responses_from_api(self, mock_api_call):
        # what does the API do when you make a request it doesn't understand, e.g. key invalid?
        # many APIs return a JSON response e.g. { "error": "missing API key"}
        # what should you app do? 
        recipe = spoonacular.get_recipe('not a food')
        # assert that the get_recipe method correctly returns a response that indicates no value 


    # option 4 - unhappy path - error connecting - API server down, no internet ... 
    # change the method name :)
    @patch('api.spoonacular.spoonacular_api_call', side_effect=Exception())  #  spoonacular_api_call will raise an exception if connection error 
    def test_api_does_whatever_it_does_when_error_connecting(self, mock_request_get):
        recipe = spoonacular.get_recipe('example food')
        # assert that the get_recipe method behave correctly if connection error 
        # maybe it returns a message, maybe it raises an exception ? 


    
    