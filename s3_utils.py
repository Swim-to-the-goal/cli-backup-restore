import boto3
import os
from config_loader import load_config


#Load S3 Config From ConfigFile 
config = load_config('config.yaml')
s3_config = config['s3']


#Create an S3 clinet with the settings in the config file
def get_s3_client():
    return boto3.client(
        's3',
        endpoint_url=f"http://{s3_config['endpoint']}",
        aws_access_key_id=s3_config['access_key'],
        aws_secret_access_key=s3_config['secret_key']
    )

#Upload the backup file to the specified backup bucket
def upload_to_minio(file_path):
    s3_client = get_s3_client()
    try:
        with open(file_path, 'rb') as file_data:
            s3_client.upload_fileobj(file_data, s3_config['backup_bucket_name'], os.path.basename(file_path))
        print(f"Uploaded {file_path} to backup bucket successfully.")
    except Exception as err:
        print(f"Error uploading to backup bucket: {err}")

#Download the backup file from the specified bucket for restore
def download_from_minio(filename, download_path):

    s3_client = get_s3_client()
    try:
        s3_client.download_file(s3_config['restore_bucket_name'], filename, download_path)
        print(f"Downloaded {filename} from restore bucket to {download_path}.")
    except Exception as err:
        print(f"Error downloading from restore bucket: {err}")
