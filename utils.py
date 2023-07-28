from datetime import datetime, timezone
import requests
from colorama import Fore


def utc_to_local(utc_dt: datetime) -> datetime:
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


def get_ip_info_by_token(ip_info_token: str) -> dict:
    res = requests.get('https://ipinfo.io', params={'token': ip_info_token})
    return res.json()


def get_current_weather_by_latitude_and_longitude(
        open_weather_api_token: str, latitude: float, longitude: float
) -> dict:
    weather = requests.get('https://api.openweathermap.org/data/2.5/weather', params={
        'lon': longitude, 'lat': latitude, 'appid': open_weather_api_token, 'units': 'metric'
    })
    return weather.json()


def print_weather_data_in_console(
        location: str,
        temp: float,
        feels_like: float,
        humidity: int,
        pressure: int,
        sunrise_time: datetime,
        sunset_time: datetime,
        current_time: datetime,
        weather_info: list[dict],
        wind_speed: float,
        wind_gust: float,
) -> None:
    current_datetime = utc_to_local(current_time)
    print(
        f'Current time: {Fore.GREEN}{current_datetime.date()} {current_datetime.time()}{Fore.RESET}\n'
        f'Your location: {Fore.RED}{location}{Fore.RESET}\n'
        f'Temperature: {Fore.BLUE}{temp}°C{Fore.RESET}. Feels like: {Fore.BLUE}{feels_like}°C{Fore.RESET}\n'
        f'Wind speed: {Fore.CYAN}{wind_speed}m/s{Fore.RESET}. Wind gust: {Fore.CYAN}{wind_gust}m/s{Fore.RESET}\n'
        f'Humidity: {Fore.YELLOW}{humidity}%{Fore.RESET}. Pressure: {Fore.YELLOW}{pressure} hPa{Fore.RESET}\n'
        f'Sunrise: {Fore.GREEN}{utc_to_local(sunrise_time).time()}{Fore.RESET}. '
        f'Sunset: {Fore.GREEN}{utc_to_local(sunset_time).time()}{Fore.RESET}'
    )
    print('Current weather:')
    for weather in weather_info:
        main = weather.get("main")
        description = weather.get("description")
        print(f'--> Weather: {Fore.BLUE}{main}{Fore.RESET}. Description: {Fore.BLUE}{description}{Fore.RESET}')
