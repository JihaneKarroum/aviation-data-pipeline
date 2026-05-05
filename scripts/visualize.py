import matplotlib.pyplot as plt
import folium
import os

def visualize_data(df):
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    # Distribution des vitesses :
    axes[0].hist(df["velocity"], bins = 10)
    axes[0].set_title("Distribution des vitesses")
    axes[0].set_xlabel("Vitesse")
    axes[0].set_ylabel("Nombre d'avions")

    # Corrélation vitesse/altitude :
    axes[1].scatter(df["velocity"], df["geo_altitude"])
    axes[1].set_title("Relation entre vitesse vs altitude")
    axes[1].set_xlabel("Vitesse")
    axes[1].set_ylabel("Altitude")
    
    # Centre Toulouse : 
    map_toulouse = folium.Map(location=[43.6, 1.44], zoom_start=7)

    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=5,
            tooltip=f"{row['origin_country']}",
            popup=f"""
            Pays: {row['origin_country']}<br>
            Vitesse: {row['velocity']}<br>
            Altitude: {row['geo_altitude']}
            """,
            color = "red" if row["flight_phase"] == "landing" else "blue",
            fill=True
        ).add_to(map_toulouse)

    
    # Phases :
    axes[2].bar(df["flight_phase"].value_counts().index,
                df["flight_phase"].value_counts().values)
    axes[2].set_title("Distribution des phases de vol")

    plt.tight_layout()

    os.makedirs("visualization", exist_ok=True)
    map_toulouse.save("visualization/toulouse_flights_map.html")
    plt.savefig("visualization/plots.png")
    
    plt.show()