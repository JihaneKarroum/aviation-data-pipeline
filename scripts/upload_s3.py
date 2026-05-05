import boto3
from datetime import datetime

def upload_file_s3(local_path, s3_key):
    s3 = boto3.client('s3')

    BUCKET_NAME = "aviation-data-jihane-bucket"

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = s3_key.split("/")[-1]
    file_name_with_time = file_name.replace(".csv", f"_{timestamp}.csv")

    s3_key_with_time = f"{'/'.join(s3_key.split('/')[:-1])}/{file_name_with_time}"

    s3.upload_file(local_path, BUCKET_NAME, s3_key_with_time)

    print(f"Uploaded: {s3_key_with_time}")