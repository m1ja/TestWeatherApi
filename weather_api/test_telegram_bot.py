import unittest
from unittest.mock import patch
from aiogram import types
from telegram_bot import (
    start_bot, stop_bot, get_start, get_weather_button, get_location, get_city, start
)

class TestTelegramBot(unittest.TestCase):
    @patch('telegram_bot.Bot.send_message')
    async def test_start_bot(self, mock_send_message):
        bot = types.Bot(token='test_token')
        await start_bot(bot)
        mock_send_message.assert_called_once_with(775860797, text='бот запушен')

    @patch('telegram_bot.Bot.send_message')
    async def test_stop_bot(self, mock_send_message):
        bot = types.Bot(token='test_token')
        await stop_bot(bot)
        mock_send_message.assert_called_once_with(775860797, text='бот остановлен')

    @patch('telegram_bot.message.answer')
    async def test_get_start(self, mock_answer):
        message = types.Message()
        await get_start(message, None)
        mock_answer.assert_called_once_with(
            'Вы попали бот который поможет вам определить погоду☀️', reply_markup=...)

    @patch('telegram_bot.message.answer')
    async def test_get_weather_button(self, mock_answer):
        message = types.Message(text='Узнать погоду☀️')
        await get_weather_button(message, None)
        mock_answer.assert_called_once_with(
            'Введите название города в котором хотите узнать погоду или нажмите...')

    @patch('telegram_bot.requests.get')
    async def test_get_location(self, mock_get):
        message = types.Message()
        message.location = types.Location(latitude=55.7558, longitude=37.6176)

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'city': 'TestCity',
            'temperature': 25,
            'pressure': 760,
            'wind_speed': 5
        }

        with patch('telegram_bot.message.answer') as mock_answer:
            await get_location(message, None)

        mock_answer.assert_called_once_with(
            'Вы находитесь в городе TestCity 🌇\n'
            'Температура на данный момент 25 🌡\n'
            'Давление на улице 760 мм рт.ст ⛅️\n'
            'Скорость ветра 5 💨'
        )

    @patch('telegram_bot.requests.get')
    async def test_get_city(self, mock_get):
        message = types.Message(text='TestCity')

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'city': 'TestCity',
            'temperature': 25,
            'pressure': 760,
            'wind_speed': 5
        }

        with patch('telegram_bot.message.answer') as mock_answer:
            await get_city(message, None)

        mock_answer.assert_called_once_with(
            'Вы находитесь в городе TestCity 🌇\n'
            'Температура на данный момент 25 🌡\n'
            'Давление на улице 760 мм рт.ст ⛅️\n'
            'Скорость ветра 5 💨'
        )

    # Add similar test functions for other bot functions

if __name__ == '__main__':
    unittest.main()

