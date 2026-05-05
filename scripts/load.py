import os
import pandas as pd
import sqlite3

def load_data(df_tls):
    conn = sqlite3.connect("database/flights.db")
    df_tls.to_sql("flights", conn, if_exists="replace", index=False)
    conn.close()
