import click
import pyfiglet 
from backup import backup_database
from restore import restore_database
from config_loader import load_config


  
result = pyfiglet.figlet_format("Backup Tools : ) ") 
print(result) 

# Load Database And S3 Configuration From Command Line Or ConfigFile
def get_db_config(db_type, host, user, password, database,port, config_path):
    if config_path:
        config = load_config(config_path)
        db_config = config.get('database', {})
        s3_config = config.get('s3', {})
    else:
        db_config = {
            'type': db_type,
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': port
        }
        s3_config = None
    
    if db_config.get('type') and db_config.get('host') and db_config.get('user') and db_config.get('password') and db_config.get('database') and db_config.get('port'):
        return db_config, s3_config
    else:
        raise click.ClickException("Database configuration is incomplete. Please provide all required options.")



# CLI Group for Database Backup and Restore operations.
@click.group()
def cli():
    pass

@cli.command()
@click.option('--db-type', help='Database type (postgresql or mysql)')
@click.option('--host', help='Database host')
@click.option('--user', help='Database user')
@click.option('--password', help='Database password')
@click.option('--database', help='Database name')
@click.option('--port', default=5432, help='Database port (default is 5432 for PostgreSQL, 3306 for MySQL)')
@click.option('--config-path', type=click.Path(), help='Path to configuration file (YAML)')


#Get Backup Func And send to Minio
def backup(db_type, host, user, password, database, port, config_path):

    try:
        db_config, _ = get_db_config(db_type, host, user, password, database, port, config_path)
        backup_database(db_config)
    except Exception as err:
        click.echo(f"Error: {err}")


#Restore Backup From Minio Bucket 

@cli.command()
@click.argument('backup_file_name')
@click.option('--db-type', help='Database type (postgresql or mysql)')
@click.option('--host', help='Database host')
@click.option('--user', help='Database user')
@click.option('--password', help='Database password')
@click.option('--database', help='Database name')
@click.option('--port',default="5432",help='Dtabase Port')
@click.option('--config-path', type=click.Path(), help='Path to configuration file (YAML)')
def restore(backup_file_name, db_type, host, user, port, password, database, config_path):

    try:
        db_config, _ = get_db_config(db_type, host, user, password, database, port, config_path)
        restore_database(db_config, backup_file_name)
    except Exception as err:
        click.echo(f"Error: {err}")

if __name__ == '__main__':
    cli()