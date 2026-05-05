import pandas as pd
import sqlite3

def analyze_data():
    conn = sqlite3.connect("database/flights.db")

    # Distribution des phases de vol :
    query_1 = "SELECT flight_phase, COUNT(*) as nb_flights " \
    "FROM flights GROUP BY flight_phase " \
    "ORDER BY nb_flights DESC"

    flights_phases = pd.read_sql(query_1, conn)
    print("- Flights phases distribution :\n", flights_phases, '\n')

    # Vitesse moyenne par phase : 
    query_2 = "SELECT flight_phase, AVG(velocity) as avg_velocity " \
    "FROM flights GROUP BY flight_phase"

    avg_velocity = pd.read_sql(query_2, conn)
    print("- Average speed per phase :\n", avg_velocity, '\n')

    # Avions en approche Toulouse : 
    query_3 = "SELECT origin_country, COUNT(*) as nb_flights " \
    "FROM flights " \
    "WHERE flight_phase = 'landing' " \
    "GROUP BY origin_country " \
    "ORDER BY nb_flights DESC"

    approach_flights = pd.read_sql(query_3, conn)
    print("- Flights in landing phase near Toulouse :\n", approach_flights, '\n')

    # Détection des anomalies : 
    query_4 = "SELECT flight_phase, velocity, geo_altitude, risk_score " \
    "FROM flights WHERE risk_score > 0"

    outliers = pd.read_sql(query_4, conn)
    if len(outliers) > 0 :
        print("- Anomalies detected :\n", outliers)
    else : 
        print("- Anomalies detection : All flights have a risk score of 0, indicating no unusual behavior.")

    conn.close()
