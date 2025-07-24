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
