import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

# access the dotenv file and get the API key. assign to variable
load_dotenv()
api_key = os.getenv('API_KEY')


@dataclass
class WeatherData:
    main: str
    description: str
    temperature: float
    feels_like: float
    temp_min: float
    temp_max: float
    humidity: float


def get_lat_lon(city_name, state_code, country_code, API_key):
    resp = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()

    data = resp[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon


def get_current_weather(lat, lon, API_key):
    resp = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data = WeatherData(
        main=resp.get('weather')[0].get('main'),
        description=resp.get('weather')[0].get('description'),
        temperature=resp.get('main').get('temp'),
        feels_like=resp.get('main').get('feels_like'),
        temp_min=resp.get('main').get('temp_min'),
        temp_max=resp.get('main').get('temp_max'),
        humidity=resp.get('main').get('humidity'),
    )
    return data


def main(city_name, state_name, country_name):
    lat, lon = get_lat_lon(city_name, state_name, country_name, api_key)
    weather_data = get_current_weather(lat, lon, api_key)
    return weather_data


if __name__ == "__main__":
    print(main())
    #lat, lon = get_lat_lon('North Vancouver', 'BC', 'Canada', api_key)
    #get_current_weather(lat, lon, api_key)