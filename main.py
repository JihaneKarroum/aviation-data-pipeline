from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data
from scripts.upload_s3 import upload_file_s3

def main():
    df = extract_data()
    df_tls = transform_data(df)
    load_data(df_tls)

    upload_file_s3("data_lake/raw/flights.csv", "raw/flights.csv")
    upload_file_s3("data_lake/processed/flights_toulouse_clean.csv", "processed/flights_toulouse_clean.csv")

if __name__ == "__main__":
    main()