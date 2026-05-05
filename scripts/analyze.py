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

'''
    # Nb vols, vitesse moyenne, altitude moyenne :
    query = "SELECT origin_country, " \
        "COUNT(*) as nb_flights, AVG(velocity) as avg_velocity, AVG(geo_altitude) as avg_altitude " \
        "FROM flights GROUP BY origin_country ORDER BY avg_velocity DESC"
    
    avg_velocity_alt = pd.read_sql(query, conn)
    print(avg_velocity_alt, '\n')

    # Combien d’avions sont en approche vs en croisière :

    query_2 = "SELECT velocity, "\
                "CASE WHEN velocity < 100 THEN 'landing/takeoff' " \
                "WHEN velocity < 200 THEN 'transition' " \
                "ELSE 'cruise'" \
                "END as flight_phase, " \
            "COUNT(*) as nb_flights " \
            "FROM flights GROUP BY flight_phase"

    phases = pd.read_sql(query_2, conn)
    print(phases, '\n')

    # Identifier les avions en phase opérationnelle sensible = avions lents + basse altitude : 
    query_3 = "SELECT icao24, " \
            "origin_country, " \
            "velocity, " \
            "geo_altitude, " \
            "CASE " \
            "WHEN velocity < 100 AND geo_altitude < 2000 THEN 'landing/takeoff' " \
            "WHEN velocity < 200 AND geo_altitude < 8000 THEN 'transition' " \
            "ELSE 'cruise' " \
            "END as risk_level, " \
            "RANK() OVER (ORDER BY geo_altitude ASC) as proximity_rank " \
    "FROM flights"

    risk = pd.read_sql(query_3, conn)
    print(risk)

    conn.close()
'''