# assembling the components

from gui import start_gui
from data import get_search, save_search, create_tables
from weather_api import get_weather
from datetime import datetime


def time_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def process_city(city):
    temp, cond = get_weather(city)
    save_search(1, city, temp, cond, time_now())
    return temp, cond


def fetch_history():
    return get_search() or []


if __name__ == "__main__":
    create_tables()
    start_gui(process_city, fetch_history)

