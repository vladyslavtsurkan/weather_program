from os import getenv

from schemas import ResponseOpenWeatherMapAPI, ResponseIpInfo
from utils import get_ip_info_by_token, get_current_weather_by_latitude_and_longitude, print_weather_data_in_console

IPINFO_TOKEN = getenv('IPINFO_TOKEN')
OPEN_WEATHER_API_KEY = getenv('OPEN_WEATHER_API_KEY')


def main():
    ip_info = get_ip_info_by_token(IPINFO_TOKEN)
    ip_info_model = ResponseIpInfo.model_validate(ip_info)
    ip_info_model.parse_loc_to_longitude_and_latitude()
    weather_info = get_current_weather_by_latitude_and_longitude(
        OPEN_WEATHER_API_KEY,
        ip_info_model.latitude,
        ip_info_model.longitude,
    )
    weather_info_model = ResponseOpenWeatherMapAPI.model_validate(weather_info)
    print_weather_data_in_console(
        weather_info_model.name,
        weather_info_model.main.temp,
        weather_info_model.main.feels_like,
        weather_info_model.main.humidity,
        weather_info_model.main.pressure,
        weather_info_model.sys.sunrise,
        weather_info_model.sys.sunset,
        weather_info_model.dt,
        [weather.model_dump() for weather in weather_info_model.weather],
        weather_info_model.wind.speed,
        weather_info_model.wind.gust
    )


if __name__ == '__main__':
    main()
