# this file will gather current hour weather data

import requests
import pandas as pd
import os

class WeatherError(Exception):
    pass

def kelvin_to_fahrenheit(kelvin_temp):
    fahrenheit_temp = (kelvin_temp - 273.15) * 9/5 + 32
    return fahrenheit_temp

def get_weather_data():
    lat = 40.81 # lon and lat of my neighborhood
    lon = -73.96
    API_key = "dcce8473543bc1bb04bfc997204c8d02"

    endpoint = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
    # print(f"[Weather Data]: Fetching from {endpoint}")

    try:
        response = requests.get(endpoint)
        response.raise_for_status()  # Raises HTTPError for bad responses 

        data = response.json()

        temp_kelvin = data['main']['temp']
        temp = kelvin_to_fahrenheit(temp_kelvin)
        temp= int(temp)

        description = data['weather'][0]['main']

        # print(f"[Weather Data]: Temperature: {temp}, Description: {description}")
        return temp,description

    except requests.exceptions.RequestException as e:
        raise WeatherError(f"Connection Error: {e}")
    except KeyError as e:
        raise WeatherError(f"Malformed Data: Missing key in JSON response: {e}")

