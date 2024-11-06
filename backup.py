import subprocess
from s3_utils import upload_to_minio


# Create Backup and Upload to Bucket_Backup Folder
def backup_database(db_config):

    backup_file = f"{db_config['database']}_backup.sql"
    try:
        if db_config['type'] == 'postgresql':
            command = f"PGPASSWORD={db_config['password']} pg_dump -h {db_config['host']} -p {db_config['port']} -U {db_config['user']} {db_config['database']} > {backup_file}"
        elif db_config['type'] == 'mysql':
            command = f"mysqldump -h {db_config['host']} -P {db_config['port']} -u {db_config['user']} -p{db_config['password']} {db_config['database']} > {backup_file}"
        subprocess.run(command, shell=True, check=True)
        print(f"Backup created: {backup_file}")
        
# Upload Backup to Minio
        upload_to_minio(backup_file)
    except subprocess.CalledProcessError as err:
        print(f"Error creating backup: {err}")
