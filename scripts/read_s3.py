import boto3
import pandas as pd
from io import StringIO

def read_latest_from_s3(bucket_name, prefix):
    s3 = boto3.client('s3')

    # Lister les fichiers :
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

    files = response.get('Contents', [])

    if not files:
        print("No files found")
        return None

    # Trier par date de modification :
    latest_file = max(files, key=lambda x: x['LastModified'])
    
    latest_key = latest_file['Key']

    print(f"Latest file: {latest_key}")

    # Lire le fichier :
    response = s3.get_object(Bucket=bucket_name, Key=latest_key)

    csv_content = response['Body'].read().decode('utf-8')

    df = pd.read_csv(StringIO(csv_content))
    print(f"Loaded dataset shape: {df.shape}")

    return df