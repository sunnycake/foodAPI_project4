import flickr
from unittest import TestCase
from unittest.mock import patch

class TestAPI(TestCase):

    @patch('api.flickr.get_image_data', return_value=[])  # fill in example no data response in the same format the API uses
    def test_api_retuns_empty_value_when_could_find_not_find_the_search(self, mock_api_call):
        result = flickr.get_image_data('$$$$$$$$$$')
        # assert that the get-image_data method correctly returns a response that indicates no value 
        self.assertEqual([], result)


    