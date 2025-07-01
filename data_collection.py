# this file get api data and stores it into a matrix for main.py to process

from citi_bike_data import get_citi_bike_data
from weather_data import get_weather_data
import datetime

def load_data():

    current_datetime = datetime.datetime.now()
    weekday_name = current_datetime.strftime("%A")
    hour_24 = current_datetime.strftime("%H")
    month_name = current_datetime.strftime("%B")


    print(f"\n\n------ GATHER DATA AT {current_datetime} ------")

    other_data = []

    print(f"[LOADING DATA]: gathering citi bike data")
    bike_stations = get_citi_bike_data()

    print(f"[LOADING DATA]: gathering weather data")
    temp, description = get_weather_data()
     

    other_data.append(temp)
    other_data.append(description)
    other_data.append(weekday_name)
    other_data.append(hour_24)
    other_data.append(month_name)

    for station in bike_stations:
        station.append(temp)
        station.append(description)
        station.append(weekday_name)
        station.append(hour_24)
        station.append(month_name) 

    return bike_stations
