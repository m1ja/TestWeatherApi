# weather_api/weather/tests.py
from django.test import TestCase
from unittest.mock import patch
from datetime import datetime, timedelta
from django.urls import reverse
from .views import get_weather_data, get_weather

class WeatherViewsTestCase(TestCase):
    def setUp(self):
        self.city_coordinates = {
            'Москва': {'lat': 55.7558, 'lon': 37.6176},
            'New York': {'lat': 40.7128, 'lon': -74.0060},
        }
        self.weather_cache = {}

    @patch('weather.views.requests.get')
    def test_get_weather_data(self, mock_get):
        # Mocking the Yandex API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'fact': {
                'temp': 20,
                'pressure_mm': 760,
                'wind_speed': 5
            }
        }

        # Call the function with specific coordinates
        result = get_weather_data(55.7558, 37.6176)

        # Assert that the function returns the expected values
        self.assertEqual(result, (20, 760, 5))

    @patch('weather.views.get_weather_data')
    def test_get_weather_view(self, mock_get_weather_data):
        # Mocking the get_weather_data function
        mock_get_weather_data.return_value = (20, 760, 5)

        # Call the view function with a GET request
        response = self.client.get(reverse('get_weather'))

        # Assert that the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Assert that the response JSON contains the expected data
        expected_data = {
            'city': None,  # Replace with the expected city name
            'temperature': 20,
            'pressure': 760,
            'wind_speed': 5
        }
        self.assertJSONEqual(str(response.content, encoding='utf-8'), expected_data)

