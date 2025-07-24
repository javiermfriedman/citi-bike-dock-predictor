"""
Javier Friedman

This file contains the functions to get the weather data for neighbordhood of stations
It uses the dotenv library to load the environment variables from the .env file.
"""

import requests
import pandas as pd
import os
from dotenv import load_dotenv


load_dotenv() 

class WeatherError(Exception):
    pass

def kelvin_to_fahrenheit(kelvin_temp):
    fahrenheit_temp = (kelvin_temp - 273.15) * 9/5 + 32
    return fahrenheit_temp

def get_weather_data():
    lat = 40.81 # lon and lat of my neighborhood
    lon = -73.96 # lon and lat of my neighborhood

    API_key = os.environ.get("WEATHER_API_KEY")
    if not API_key:
        raise ValueError("API key not found. Please set the WEATHER_API_KEY environment variable.")

    endpoint = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
    
    try:
        response = requests.get(endpoint)
        response.raise_for_status()  

        data = response.json()

        temp_kelvin = data['main']['temp']
        temp = kelvin_to_fahrenheit(temp_kelvin)
        temp= int(temp)

        description = data['weather'][0]['main']

        return temp,description

    except requests.exceptions.RequestException as e:
        raise WeatherError(f"Connection Error: {e}")
    except KeyError as e:
        raise WeatherError(f"Malformed Data: Missing key in JSON response: {e}")