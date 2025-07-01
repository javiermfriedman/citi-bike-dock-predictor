import os
from data_collection import load_data
import pandas as pd

if __name__ == "__main__":
    data = load_data()

    # Define column names based on the order data is appended in data_collection.py
    column_names = [
        "Station Name",
        "Empty Slots",
        "E-bikes Available",
        "Temperature (F)",
        "Weather Description",
        "Weekday",
        "Hour (24-hour)"
    ]

    # Define the directory for saving CSV files
    output_directory = "data"

    # Create the directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Loop through each station's data
    for station_data in data:
        # The station name is the first element in each station's data list
        station_name = station_data[0]

        # Sanitize the station name to be a valid filename
        sanitized_station_name = "".join(c if c.isalnum() else "_" for c in station_name)
        
        # Construct the full path for the CSV file within the output directory
        csv_file_path = os.path.join(output_directory, f"{sanitized_station_name}_data.csv")

        # Create a DataFrame for the current station's new data
        new_df = pd.DataFrame([station_data], columns=column_names)

        # Check if the CSV file already exists
        if os.path.exists(csv_file_path):
            # If it exists, load the existing data
            try:
                existing_df = pd.read_csv(csv_file_path)
                # Append the new data to the existing DataFrame
                combined_df = pd.concat([existing_df, new_df], ignore_index=True)
                # Save the combined DataFrame back to the CSV file
                combined_df.to_csv(csv_file_path, index=False)
            except pd.errors.EmptyDataError:
                # Handle case where file exists but is empty
                new_df.to_csv(csv_file_path, index=False)
                print(f"Created new file for '{station_name}' (existing file was empty) at {csv_file_path}")
            except Exception as e:
                print(f"Error processing {csv_file_path}: {e}. Saving new data as a new file.")
                new_df.to_csv(csv_file_path, index=False) # Fallback to overwrite if error
        else:
            # If the file doesn't exist, create a new one
            new_df.to_csv(csv_file_path, index=False)
            print(f"Created new file for '{station_name}' at {csv_file_path}")

    print(f"\nAll station data processed and saved/appended in the '{output_directory}' directory.")
