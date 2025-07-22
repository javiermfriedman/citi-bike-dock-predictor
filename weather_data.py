# this file will gather current hour weather data

import requests
import pandas as pd
import os
from dotenv import load_dotenv # Import the dotenv library

# Load variables from a .env file for local testing
load_dotenv() 

class WeatherError(Exception):
    pass

def kelvin_to_fahrenheit(kelvin_temp):
    fahrenheit_temp = (kelvin_temp - 273.15) * 9/5 + 32
    return fahrenheit_temp

def get_weather_data():
    lat = 40.81 # lon and lat of my neighborhood
    lon = -73.96 # lon and lat of my neighborhood

    # --- MODIFICATION START ---
    # Read the API key from an environment variable named "WEATHER_API_KEY"
    API_key = os.environ.get("WEATHER_API_KEY")

    # Fail gracefully if the API key is not found
    if not API_key:
        raise ValueError("API key not found. Please set the WEATHER_API_KEY environment variable.")
    # --- MODIFICATION END ---

    endpoint = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
    
    try:
        response = requests.get(endpoint)
        response.raise_for_status()  # Raises HTTPError for bad responses 

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