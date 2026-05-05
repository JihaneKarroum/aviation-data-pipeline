from scripts.read_s3 import read_latest_from_s3
from scripts.analyze import analyze_data
from scripts.visualize import visualize_data

def main():
    df = read_latest_from_s3(
        "aviation-data-jihane-bucket",
        "processed/"
    )

    analyze_data()
    visualize_data(df)

if __name__ == "__main__":
    main()