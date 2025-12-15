# for experiments and trials

import json

with open("config.json") as f:
    config = json.load(f)

api_key  = config["weather_api_key"]
print(api_key)