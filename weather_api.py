# to get info of weather of a city

import requests as req
import json


def get_weather(city):
    with open("config.json") as f:
        config = json.load(f)
    api_key = config["weather_api_key"]
    if api_key is None:
        raise RuntimeError("wrather api key not found")

    url = "https://api.weatherapi.com/v1/current.json"

    param = {"key": api_key, "q": city}

    res = req.get(url, params=param)

    if res.status_code != 200:
        raise RuntimeError("weather api request failed")
    else:
        info = res.json()
        return (info["current"]["temp_c"], info["current"]["condition"]["text"])
