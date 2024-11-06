import subprocess
from s3_utils import download_from_minio
import os


#Restore the database from the backup file downloaded from the specified bucket to restore
def restore_database(db_config, backup_file_name):

    download_path = f"./{backup_file_name}"
    download_from_minio(backup_file_name, download_path)

#Execution of the restore command based on the type of database
    try:

        if db_config['type'] == 'postgresql':
            command = f"PGPASSWORD={db_config['password']} psql -h {db_config['host']} -U {db_config['user']} -d {db_config['database']} -f {download_path}"
        elif db_config['type'] == 'mysql':
            command = f"mysql -h {db_config['host']} -u {db_config['user']} -p{db_config['password']} {db_config['database']} < {download_path}"
        subprocess.run(command, shell=True, check=True)
        print(f"Database restored from {backup_file_name}")
    except subprocess.CalledProcessError as err:
        print(f"Error restoring database: {err}")
        # Delete the downloaded file after recovery
    finally:
        if os.path.exists(download_path):
            os.remove(download_path)
