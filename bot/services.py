import requests
import random
import aiohttp
import asyncio

# --------------------------------------------------------------------------------

api_key = "c89b27804c7c4ae18a8a3123a3584c6f"

q_list = ["Apple", "Amazon", "Netflix", "USA", "Ukraine", "Chechnya"]


def get_top_headlines(q=q_list):
    base_url = "https://newsapi.org/v2/top-headlines?sources=bbc-news"

    params = {
        "apiKey": api_key,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        news_data = response.json()
        new = news_data["articles"][random.randint(0, 9)]
        return f"{new['title']}:\n{new['description']}"
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# --------------------------------------------------------------------------------


def get_coordinates(city_name):
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    api_key = "66541fe9-9088-4352-97b9-bf1533fb7de6"

    params = {
        "format": "json",
        "apikey": api_key,
        "geocode": city_name,
    }

    response = requests.get(geocode_url, params=params)

    if response.status_code == 200:
        geodata = response.json()
        coordinates = geodata["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
        latitude, longitude = map(float, coordinates.split())
        return latitude, longitude
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None, None


def get_weather_data(city_name, language="ru_RU"):
    longitude, latitude = get_coordinates(city_name)
    base_url = f"https://api.weather.yandex.ru/v2/forecast/?lat={latitude}&lon={longitude}&lang={language}"
    api_key = "e45e66f5-23fa-4369-adb1-e636743f5c77"

    headers = {
        "X-Yandex-API-Key": api_key,
    }

    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data["fact"]["temp"]
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# --------------------------------------------------------------------------------


async def create_telegram_message(message_id, from_user_id, chat_id, text):
    url = "http://localhost:8000/api/create_telegram_message/"

    data = {
        "message_id": message_id,
        "from_user_id": from_user_id,
        "chat_id": chat_id,
        "text": text
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            if response.status == 201:
                return await response.json()
            else:
                return None


# --------------------------------------------------------------------------------


async def get_commands_list():
    url = "http://localhost:8000/list/commands/"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None



#----------------------------------------------------------------