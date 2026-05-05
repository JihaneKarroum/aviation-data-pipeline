import os
import pandas as pd

# Flight phase : 
'''
altitude < 2000 ET vitesse > 180 → takeoff
altitude < 2000 ET vitesse ≤ 180 → landing
2000 ≤ altitude < 8000 → transition
Altitude ≥ 8000       → cruise
'''

def classify_phase(row):
    altitude = row["geo_altitude"]
    velocity = row["velocity"]
    
    if altitude < 2000:
        if velocity > 180:
            return "takeoff"
        else:
            return "landing"
    elif altitude < 8000:
        return "transition"
    else:
        return "cruise"


# Détection d’approche :
def detect_approach(df_tls):
    approaching_flights = df_tls[df_tls["flight_phase"] == "landing"]
    return approaching_flights

# Risk Score : 
def compute_risk(row):
    risk = 0
    
    phase = row["flight_phase"]
    velocity = row["velocity"]
    
    # anomalie en cruise (lent en altitude)
    if phase == "cruise" and velocity < 100:
        risk += 1
        
    # anomalie en landing (trop rapide)
    if phase == "landing" and velocity > 200:
        risk += 1
        
    return risk


''' 
Filtre Toulouse par coordonnées GPS: 
    Latitude  ≈ 43.6
    Longitude ≈ 1.44
'''
def transform_data(df):
    df = df.dropna(subset=["velocity", "geo_altitude", "latitude", "longitude"])

    df_toulouse = df[
        (df["latitude"].between(43.0, 44.5)) &
        (df["longitude"].between(1, 2.5))
    ].copy()

    # enlever valeurs absurdes
    df_toulouse = df_toulouse[df_toulouse["geo_altitude"] >= 0]
    df_toulouse = df_toulouse[df_toulouse["geo_altitude"] < 20000]
    df_toulouse = df_toulouse[df_toulouse["velocity"] > 0]  
    
    df_toulouse["flight_phase"] = df_toulouse.apply(classify_phase, axis=1)  
    df_toulouse["risk_score"] = df_toulouse.apply(compute_risk, axis=1)

    os.makedirs("data_lake/processed", exist_ok=True)

    df_toulouse.to_csv("data_lake/processed/flights_toulouse_clean.csv", index=False)
        
    return df_toulouse
