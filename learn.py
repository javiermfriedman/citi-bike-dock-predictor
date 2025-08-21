from database.supabase_client import get_station
import pandas as pd 
from sklearn.model_selection import train_test_split


station_name = "Lenox Ave & W 115 St"
data = get_station(station_name)

df = pd.DataFrame(data)
print(df.head())

X = df[["empty_slots", "temperature_f", "weekday", "hour", "month", "weather_description"]]
y = df["ebikes_available"]

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

print("test")