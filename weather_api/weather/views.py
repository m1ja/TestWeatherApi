from django.http import JsonResponse
from django.views.decorators.http import require_GET
import requests
from datetime import datetime, timedelta

weather_cache = {}

# Словарь с координатами городов (замените на актуальные координаты)
city_coordinates = {
    'Москва': {'lat': 55.7558, 'lon': 37.6176},
    'New York': {'lat': 40.7128, 'lon': -74.0060},
}

def get_weather_data(lat, lon):
    # Запрос данных о погоде от Yandex
    headers = {"X-Yandex-API-Key": 'd6487248-be4d-40e2-a125-77621045e5ec'}
    yandex_url = f"https://api.weather.yandex.ru/v2/informers?lat={lat}&lon={lon}"
    response = requests.get(yandex_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        fact = data.get('fact')
        temperature = fact.get('temp')
        pressure = fact.get('pressure_mm')
        wind_speed = fact.get('wind_speed')
        return temperature, pressure, wind_speed
    else:
        print(f"Failed to retrieve weather data. Status code: {response.status_code}")
        return None

@require_GET
def get_weather(request):
    city_name = request.GET.get('city')
    print(city_name)
    # Извлечение координат
    if city_name is not None:
        coordinates = city_coordinates[city_name]
        lat, lon = coordinates['lat'], coordinates['lon']
    else:
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')

    # Проверка кэша
    cache_key = f"{lat},{lon}"
    if cache_key in weather_cache and weather_cache[cache_key]['expires'] > datetime.now():
        weather_data = weather_cache[cache_key]['data']
    else:
        weather_data = get_weather_data(lat, lon)
        if weather_data:
            # Обновление кэша
            cache_duration = 1800  # 30 минут
            expiration_time = datetime.now() + timedelta(seconds=cache_duration)
            weather_cache[cache_key] = {'data': weather_data, 'expires': expiration_time}

    if weather_data:
        return JsonResponse({
            'city': city_name,
            'temperature': weather_data[0],
            'pressure': weather_data[1],
            'wind_speed': weather_data[2]
        })
    else:
        return JsonResponse({'error': 'Failed to retrieve weather data'}, status=500)