from api import nutritionix
from unittest import TestCase
from unittest.mock import patch

class testAPI(TestCase):

    # Testing the wrong entity 
    @patch('api.nutritionix.nutritionix_api_call', return_value=['Pepsi'])  
    def test_api_does_whatever_it_does_when_wrong_results(self, mock_api_call):
        result = nutritionix.get_drink('#$4@')
        self.assertNotEqual('Pepsi', result)

    # testing an error connectig to the API 
    @patch('requests.get')
    def test_request_response_status_code(self, mock_requests_get):
        mock_requests_get.return_value.status_code = 404 

        self.assertNotEqual(mock_requests_get, 'error')

    # Testing an Empty 
    @patch('requests.get')
    def test_request_response_status_code_returning_empy(self, mock_requests_get):
        mock_requests_get.return_value.status_code = [] 
        response = nutritionix.get_drink("Pepsi")

        self.assertNotEqual(response, [])

    # Testing an existing data 
    @patch('api.nutritionix.nutritionix_api_call')
    def test_api_returns_data_if_data_exists(self, mock_requests_get):
        mock_requests_get.return_value.status_code = ["Sweetened Green Tea "] 
        response = nutritionix.get_drink("search_term")

        self.assertTrue(response,  mock_requests_get.return_value.status_code)

if __name__ == '__main__':
   unittest.main()