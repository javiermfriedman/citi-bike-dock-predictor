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

## Automating with GitHub Actions

You can automate data collection to run hourly using GitHub Actions. Here’s how to set it up:

### 1. Create the Workflow File
- In your project root, create the directory (if it doesn’t exist):
  ```
  .github/workflows/
  ```
- Inside that directory, create a file named `collect_data.yml`.

### 2. Example Workflow: `.github/workflows/collect_data.yml`
```yaml
name: Collect Citi Bike Data Hourly

on:
  schedule:
    - cron: '0 * * * *'  # Runs at the top of every hour
  workflow_dispatch:      # Allows manual triggering from the GitHub UI

jobs:
  run-script:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run main.py
        env:
          WEATHER_API_KEY: ${{ secrets.WEATHER_API_KEY }}
          SUPABASE_URL: ${{ secrets.SUPABASE_URL }}
          SUPABASE_KEY: ${{ secrets.SUPABASE_KEY }}
        run: python main.py
```

### 3. Add Your Secrets
- Go to your GitHub repository on the web.
- Click **Settings** → **Secrets and variables** → **Actions**.
- Add the following secrets:
  - `WEATHER_API_KEY`
  - `SUPABASE_URL`
  - `SUPABASE_KEY`

These will be available to your workflow as environment variables.

### 4. Commit and Push
Add, commit, and push the new workflow file:
```sh
git add .github/workflows/collect_data.yml
git commit -m "Add GitHub Actions workflow to run data collection hourly"
git push origin main
```

Your script will now run every hour on GitHub Actions, using the secrets you provided.

## Future Work

- Build and train a linear regression model to predict e-bike availability.
- Expand to more stations or additional data sources.
- Automate data collection with a reliable cloud scheduler.

---

*For questions or contributions, please open an issue or submit a pull request.*