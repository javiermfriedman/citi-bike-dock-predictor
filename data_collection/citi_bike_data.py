""" 
Javier Friedman

This file contains the functions to get the citi bike data for my desired stations.
"""

import requests
import pandas as pd
import numpy as np

class TransportError(Exception):
	pass

def filter_station(name):  # return true if its the station we want
	my_stations = ["Lenox Ave & W 115 St",
					"Lenox Ave & W 117 St",
					"Adam Clayton Powell Blvd & W 115 St",
					"Adam Clayton Powell Blvd & W 118 St",
					"Mt Morris Park W & W 120 St"]
	if name in my_stations:
		return True
	else:
		return False
	

def get_citi_bike_data():
	endpoint = "https://api.citybik.es/v2/networks/citi-bike-nyc"
	try:
		response = requests.get(endpoint)
		if response.status_code != 200:
				raise TransportError("Invalid Response")
		
		data = response.json()
		stations = data['network']['stations']
		
		my_stations_data = []
		for station in stations:
			station_name = station.get("name")
			empty_slots = station.get("empty_slots")
			# print(f"looking at station: {station_name}")
			if filter_station(station_name): # if its my station return the data
				extra = station.get("extra", {})
				my_stations_data.append([
					station_name,
					empty_slots,
					extra.get("ebikes", 0),
				])

	
		return my_stations_data
		
	except requests.exceptions.RequestException:
		raise TransportError("Connection Error")
	except KeyError:
		raise TransportError("Malformed Data")
		