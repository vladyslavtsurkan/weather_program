from datetime import datetime

from pydantic import BaseModel, Field


class CloudsResponseWeatherMapAPI(BaseModel):
    all: int


class CoordResponseWeatherMapAPI(BaseModel):
    lat: float
    lon: float


class MainResponseWeatherMapAPI(BaseModel):
    feels_like: float
    grnd_level: int
    humidity: int = Field(lte=100, gte=0)
    pressure: int
    sea_level: int
    temp: float
    temp_max: float
    temp_min: float


class SysResponseWeatherMapAPI(BaseModel):
    country: str
    sunrise: datetime
    sunset: datetime


class WeatherResponseWeatherMapAPI(BaseModel):
    id: int
    icon: str
    main: str
    description: str


class WindResponseWeatherMapAPI(BaseModel):
    deg: int
    gust: float
    speed: float


class ResponseOpenWeatherMapAPI(BaseModel):
    base: str
    clouds: CloudsResponseWeatherMapAPI
    cod: int
    coord: CoordResponseWeatherMapAPI
    dt: datetime
    id: int
    main: MainResponseWeatherMapAPI
    name: str
    sys: SysResponseWeatherMapAPI
    timezone: int
    visibility: int
    weather: list[WeatherResponseWeatherMapAPI]
    wind: WindResponseWeatherMapAPI
