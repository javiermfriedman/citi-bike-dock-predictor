"""
Javier Friedman

This file contains the functions to insert the station data into the Supabase database.
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
TABLE_NAME = "citi_bike_data"

def insert_record(payload: dict):
    """Insert a single row into the Supabase table."""
    url = f"{SUPABASE_URL}/rest/v1/citi_bike_data"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code >= 400:
        print(f"[ERROR] Supabase insert failed: {response.status_code} — {response.text}")
    else:
        print(f"[✅ INSERTED] {payload['station_name']} @ {payload['hour']}h")

def get_station(station_name: str):
    """
    Fetch all rows from the table for a given station_name.
    Returns a list of dicts (rows).
    """
    url = f"{SUPABASE_URL}/rest/v1/{TABLE_NAME}"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Accept": "application/json"
    }
    params = {
        "station_name": f"eq.{station_name}"  # PostgREST filter syntax
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code >= 400:
        print(f"[ERROR] Supabase fetch failed: {response.status_code} — {response.text}")
        return []
    
    data = response.json()
    print(f"[FETCHED] {len(data)} rows for station '{station_name}'")
    return data

