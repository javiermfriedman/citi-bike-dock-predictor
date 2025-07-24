# Citi Bike Open Data Predictor

## Overview

This project collects real-time Citi Bike station data and local weather information for select stations in New York City. The primary objective is to build a robust dataset for future machine learning analysis—specifically, to perform linear regression to predict the availability of e-bikes ("super bikes") at these stations based on time, weather, and other contextual factors. 

reason: citibike is my main form of transportation so I want to know when there will
be availlabilty

## Project History

- **Initial Approach:** Data collection was first automated using a cron job on a local machine, but this method proved unreliable because it required my computer to alwasy be on.
- **GitHub Workflows:** The next attempt used GitHub Actions to automate data collection, but this was hindered by difficulties configuring Git Large File Storage (LFS) for the growing dataset.
- **Current Solution:** The project now leverages Supabase, a cloud database, to store collected data reliably and scalably.

## Architecture
The project is organized into modular Python scripts:

- **Data Collection:** Fetches Citi Bike and weather data, processes it, and prepares it for storage.
- **Database Integration:** Inserts the processed data into a Supabase database.
- **Main Script:** Orchestrates the data collection and storage process.

## File Descriptions

- **main.py**  
  Entry point of the project. Orchestrates data collection and inserts results into the Supabase database.

- **data_collection/data_collection.py**  
  Coordinates the collection of Citi Bike and weather data, combines them, and formats them for storage.

- **data_collection/citi_bike_data.py**  
  Fetches real-time data from the Citi Bike API for a predefined set of stations and extracts relevant information (station name, empty slots, e-bikes available).

- **data_collection/weather_data.py**  
  Fetches current weather data for the neighborhood of the selected stations using the OpenWeatherMap API.

- **database/supabase_client.py**  
  Handles the connection to Supabase and provides a function to insert new records into the database.

- **requirements.txt**  
  Lists the Python dependencies required to run the project.

- **README.md**  
  Project documentation, including purpose, history, architecture, and usage instructions.

## Usage

1. **Set up environment variables:**  
   Create a `.env` file in the project root with your API keys:
   ```
   WEATHER_API_KEY=your_openweathermap_api_key
   SUPABASE_URL=https://your-project-ref.supabase.co
   SUPABASE_KEY=your_supabase_api_key
   ```

2. **Install dependencies:**  
   ```
   pip install -r requirements.txt
   ```

3. **Run the main script:**  
   ```
   python main.py
   ```

## Future Work

- Build and train a linear regression model to predict e-bike availability.
- Expand to more stations or additional data sources.
- Automate data collection with a reliable cloud scheduler.

---

*For questions or contributions, please open an issue or submit a pull request.*