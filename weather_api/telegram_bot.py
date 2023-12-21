import asyncio
import requests
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, F
from weather.views import get_weather, get_weather_data

token = '1547511727:AAEhsio1Kah0QVaNHLE6c_JHbExAy8plm2k'

keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Узнать погоду☀️'
        )
    ]
], resize_keyboard=True)

keyboard_location = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Поделиться местоположением 📍',
            request_location=True
        )
    ]
], resize_keyboard=True)

async def start_bot(bot: Bot):
    await bot.send_message(775860797, text='бот запушен')


async def stop_bot(bot: Bot):
    await bot.send_message(775860797, text='бот остановлен')


async def get_start(message: Message, bot: Bot):
    await message.answer('Вы попали бот который поможет вам определить погоду☀️', reply_markup=keyboard)


async def get_weather_button(messge: Message, bot: Bot):
    await messge.answer('Введите название города в котором хотите узнать погоду или нажмите на кнопку "Поделиться местоположение" что бы узнать погоду в текущем месте', reply_markup=keyboard_location)


async def get_location(message: Message, bot: Bot):
    weather = f"http://127.0.0.1:8000/weather?lat={message.location.latitude}&lon={message.location.longitude}"
    response = requests.get(weather)
    if response.status_code == 200:
        data = response.json()
        city = data.get('city')
        temperature = data.get('temperature')
        pressure = data.get('pressure')
        wind_speed = data.get('wind_speed')
    else:
        await message.answer('Что то пошло не так')
    if city is not None:
        await message.answer(f'Вы находитесь в городе {city} 🌇\n'
                             f'Температура на данный момент {temperature} 🌡\n'
                             f'Давление на улице {pressure} мм рт.ст ⛅️\n'
                             f'Скорость ветра {wind_speed} 💨')
    else:
        await message.answer(f'Город неизвестен 🙁\n'
                             f'Температура на данный момент {temperature} 🌡\n'
                             f'Давление на улице {pressure} мм рт.ст ⛅️\n'
                             f'Скорость ветра {wind_speed} 💨')


async def get_city(message: Message, bot: Bot):
    weather = f"http://127.0.0.1:8000/weather?city={message.text}"
    response = requests.get(weather)
    if response.status_code == 200:
        data = response.json()
        city = data.get('city')
        temperature = data.get('temperature')
        pressure = data.get('pressure')
        wind_speed = data.get('wind_speed')
    else:
        await message.answer('Что то пошло не так')
    if city is not None:
        await message.answer(f'Вы находитесь в городе {city} 🌇\n'
                             f'Температура на данный момент {temperature} 🌡\n'
                             f'Давление на улице {pressure} мм рт.ст ⛅️\n'
                             f'Скорость ветра {wind_speed} 💨')
    else:
        await message.answer(f'Город неизвестен 🙁\n'
                             f'Температура на данный момент {temperature} 🌡\n'
                             f'Давление на улице {pressure} мм рт.ст ⛅️\n'
                             f'Скорость ветра {wind_speed} 💨')



async def start():
    bot = Bot(token=token)

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_location, F.location)
    dp.message.register(get_weather_button, F.text == 'Узнать погоду☀️')
    dp.message.register(get_start, Command('start'))
    dp.message.register(get_city)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())