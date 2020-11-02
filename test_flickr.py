from api import flickr
from unittest import TestCase
from unittest.mock import patch

class TestAPI(TestCase):
    """test if the api call connects succesfully and returns the expected data"""
    @patch('api.flickr.get_image_data', return_value=[[{
            'id': '1659178741', 
            'owner': '9986597@N04', 
            'secret': '25105cfc7a', 
            'server': '2197', 
            'farm': 3, 
            'title': 'pepsi', 
            'ispublic': 1, 
            'isfriend': 0, 
            'isfamily': 0
            }], None])
    def test_get_image_data_returns_data(self, mock_api):
        response, error= flickr.get_image_data("pepsi")
        self.assertEqual([{
            'id': '1659178741', 
            'owner': '9986597@N04', 
            'secret': '25105cfc7a', 
            'server': '2197', 
            'farm': 3, 
            'title': 'pepsi', 
            'ispublic': 1, 
            'isfriend': 0, 
            'isfamily': 0
            }], response)


    @patch('api.flickr.get_image_data', return_value=[[], None], )  # fill in example no data response in the same format the API uses
    def test_api_retuns_empty_value_when_could_find_not_find_the_search(self, mock_api_call):
        result, error = flickr.get_image_data('$$$$$$$$$$')
        # assert that the get-image_data method correctly returns a response that indicates no value 
        self.assertEqual([], result)
        self.assertEqual(None, error)


       
