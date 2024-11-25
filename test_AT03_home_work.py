import pytest
from unittest.mock import patch
from main_AT03_home_work import get_random_cat_image


def test_get_random_cat_image_success():
    mock_response = [{"id": "MTk3NDc4MQ", "url": "https://cdn2.thecatapi.com/images/MTk3NDc4MQ.jpg"}]

    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = get_random_cat_image()

        assert result == "https://cdn2.thecatapi.com/images/MTk3NDc4MQ.jpg"
        mock_get.assert_called_once_with("https://api.thecatapi.com/v1/images/search")

def test_get_random_cat_image_failure():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = []

        result = get_random_cat_image()

        assert result is None
        mock_get.assert_called_once_with("https://api.thecatapi.com/v1/images/search")
