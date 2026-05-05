# ✈️ Aviation Data Pipeline (Python + SQL + AWS S3)

## 📌 Overview

This project builds an end-to-end data pipeline using real-time aviation data.
It demonstrates how to collect, process, store, analyze, and visualize flight data while extracting meaningful operational insights.

This project demonstrates a complete data engineering workflow, from data ingestion to cloud storage and analytical insights.

The project focuses on **air traffic analysis around Toulouse**, combining geospatial filtering with flight behavior interpretation.

⚠️ **Important:**
The dataset is dynamically retrieved from an API.
Therefore, **results and insights may vary depending on the data available at runtime**.

---

## 🚀 Project Objectives

* Ingest real-time flight data from an external API
* Clean and filter geospatial data (Toulouse area)
* Classify flight phases based on altitude and speed
* Store data in a cloud-based data lake (AWS S3)
* Perform SQL-based analysis
* Visualize flight patterns and distributions
* Detect potentially unusual flight behavior

---

## 🧱 Architecture

```text
API → Extraction → Transformation → Storage (S3 + SQLite)
                                  ↓
                             SQL Analysis
                                  ↓
                             Visualization
```

---

## ⚙️ Tech Stack

* **Python** (Pandas, Requests, Boto3)
* **SQL** (SQLite)
* **AWS S3** (Cloud storage)
* **Matplotlib / Folium** (Visualization)

---

## 📂 Project Structure

```text
aviation-data-pipeline/
│
├── data_lake/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── analyze.py
│   ├── visualize.py
│   ├── upload_s3.py
│   └── read_s3.py
│
├── database/
│   └── flights.db
│
├── visualization/
│   ├── plots.png
│   └── toulouse_flights_map.html
│
├── main.py
├── read_pipeline.py
└── README.md
```

---

## 🔄 Pipeline Execution

This project is structured into two separate pipelines:

### 1. Data Ingestion Pipeline (`main.py`)

* Extracts data from the API
* Cleans and transforms data
* Stores data in SQLite
* Uploads raw and processed data to AWS S3 (with timestamp versioning)

### 2. Data Analysis Pipeline (`read_pipeline.py`)

* Reads the latest dataset from AWS S3
* Performs SQL-based analysis
* Generates visualizations and insights

This separation reflects real-world data engineering workflows where data production and data consumption are handled independently.

---

## 🔄 Pipeline Steps

### 1. Data Extraction

* Data retrieved from OpenSky API
* Stored as raw CSV

### 2. Data Transformation

* Filtering flights near Toulouse using GPS coordinates
* Removing invalid or inconsistent values
* Feature engineering:

  * Flight phase classification (takeoff, landing, transition, cruise)
  * Risk score based on simple behavioral rules

### 3. Data Storage

* Processed data stored in:

  * SQLite database
  * AWS S3 (data lake with versioning)

### 4. Data Analysis

* SQL queries used to analyze:

  * Flight phase distribution
  * Average velocity by phase
  * Flights in landing phase near Toulouse
  * Detection of anomalies

### 5. Visualization

* Velocity distribution (histogram)
* Velocity vs altitude (scatter plot)
* Flight phase distribution (bar chart)
* Interactive map of flights around Toulouse

---

## 📊 Visualizations

Generated visual outputs are available in the `/visualization` folder:

- `plots.png`: velocity distribution, altitude correlation and flight phase distribution  
- `toulouse_flights_map.html`: interactive map of flights near Toulouse  
  You can open the HTML file in a browser to explore the interactive map.

---

## 📊 Data Analysis & Insights

The following insights are based on the latest dataset retrieved from the API at runtime.

### 📦 Dataset Overview

The dataset contains **18 flight observations** filtered around the Toulouse area.

⚠️ Since the data is retrieved in real time,
**results may change depending on when the pipeline is executed**.

---

### ✈️ Flight Phase Distribution

* **Cruise:** 11 flights
* **Landing:** 4 flights
* **Transition:** 3 flights

Most aircraft are in cruise phase, which is expected as flights spend most of their time at high altitude.

---

### 🚀 Velocity Analysis

Average velocity per phase:

* **Cruise:** ~233 m/s
* **Transition:** ~120 m/s
* **Landing:** ~88 m/s

This confirms that aircraft:

* Maintain high speed during cruise
* Gradually reduce speed during descent
* Reach low speeds during landing

---

### 📈 Velocity vs Altitude Relationship

The analysis shows a strong relationship between altitude and velocity:

* High altitude → high velocity
* Low altitude → reduced velocity

This reflects real-world aviation behavior.

---

### 🛬 Flights Near Toulouse

All flights detected in landing phase near Toulouse originate from France.

This suggests **regional or domestic traffic patterns**, consistent with expected air traffic around Toulouse.

---

### 🗺️ Geospatial Visualization

An interactive map displays aircraft positions around Toulouse with:

* Latitude & longitude
* Velocity
* Altitude

This provides a clear spatial overview of air traffic in the region.

---

### ⚠️ Anomaly Detection

A rule-based risk scoring system was implemented using flight phase and velocity.

**Result:**

> No anomalies were detected in this dataset.

This indicates:

* Consistent and realistic flight behavior
* No unusual patterns in the current data sample

⚠️ Note:
Anomaly detection is limited by dataset size and may vary with larger datasets.

---

## ☁️ Cloud Integration (AWS S3)

* Created an S3 bucket to simulate a data lake
* Implemented timestamp-based file versioning
* Stored raw and processed datasets
* Retrieved the latest dataset automatically using S3 metadata

---

## 🔐 Security

* AWS credentials are configured locally
* No sensitive data is exposed in the repository

---

## 💡 What I Learned

* Building a complete ETL pipeline
* Cleaning and structuring real-world data
* Designing meaningful data analysis
* Using SQL for exploration
* Integrating cloud storage (AWS S3)
* Translating data into business insights

---

## 📎 Future Improvements

* Use larger datasets for more robust analysis
* Implement real-time streaming
* Replace SQLite with PostgreSQL
* Add orchestration (Airflow)
* Build an interactive dashboard (Streamlit / Power BI)

---

## 🧠 Author

Data engineering student building practical, real-world projects using Python, SQL, and Cloud technologies.
