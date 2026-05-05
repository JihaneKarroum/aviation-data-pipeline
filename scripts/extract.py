import os
import requests
import pandas as pd

def extract_data():
    url = "https://opensky-network.org/api/states/all"

    response = requests.get(url)
    data = response.json()

    flights = data["states"]

    columns = [
    "icao24", "callsign", "origin_country", "time_position",
    "last_contact", "longitude", "latitude", "baro_altitude",
    "on_ground", "velocity", "heading", "vertical_rate",
    "sensors", "geo_altitude", "squawk", "spi", "position_source"
    ]

    df = pd.DataFrame(flights, columns=columns)
    
    os.makedirs("data_lake/raw", exist_ok=True)
    df.to_csv('data_lake/raw/flights.csv', index=False)

    return df