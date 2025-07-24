from database.supabase_client import insert_record
from data_collection.data_collection import load_data
from datetime import datetime

def main():

    bike_stations_data = load_data()

    # [station_name, empty_slots, ebikes, temp, description, weekday, hour, month]
    for station_data in bike_stations_data:

        payload = {
                "station_name": station_data[0],
                "empty_slots": int(station_data[1]),
                "ebikes_available": int(station_data[2]),
                "temperature_f": float(station_data[3]),
                "weather_description": station_data[4],
                "weekday": station_data[5],
                "hour": station_data[6],
                "month": station_data[7]
            }
        # print(payload)
        insert_record(payload)


if __name__ == "__main__":
    main()
