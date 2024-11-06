
# Database Backup and Restore CLI

A simple and efficient command-line interface (CLI) tool for managing database backups and restores. This tool supports PostgreSQL and MySQL databases, and allows you to store backups in an S3-compatible storage like MinIO.

## Features
- **Backup & Restore**: Easily back up and restore databases (PostgreSQL, MySQL).
- **S3 Integration**: Store backups in MinIO (or any S3-compatible storage).
- **Configuration Options**: Use command-line options or a YAML configuration file.
- **Error Handling**: Handles common errors with helpful error messages.
- **Custom Port Support**: Specify custom database ports for flexibility.
- **Flexible Input**: Provide database details through CLI options or configuration file.

## Table of Contents
1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Usage](#usage)
4. [Example Commands](#example-commands)
5. [Roadmap](#roadmap)
6. [Contributing](#contributing)
7. [License](#license)

---

## Installation

### Prerequisites
- **Python 3.7+**
- **PostgreSQL** or **MySQL** client tools
- **MinIO or any S3-compatible storage** for remote backup storage

1. Clone this repository:
   ```bash
   git clone https://github.com/Swim-to-the-goal/db-backup-cli.git
   cd db-backup-cli
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

You can configure the CLI either through command-line options or by creating a YAML configuration file.

### YAML Configuration File (config.yaml)

```yaml
database:
  type: "postgresql"       # Options: "postgresql" or "mysql"
  host: "localhost"
  port: 5432               # Default: 5432 for PostgreSQL, 3306 for MySQL
  user: "your_user"
  password: "your_password"
  database: "your_database"

s3:
  endpoint: "localhost:9000"
  access_key: "minio-access-key"
  secret_key: "minio-secret-key"
  backup_bucket_name: "backup-bucket"
  restore_bucket_name: "restore-bucket"
```

## Usage

### Backup Command

```bash
python main.py backup --config-path config.yaml
```

Or provide details directly via CLI:

```bash
python main.py backup --db-type postgresql --host localhost --port 5432 --user your_user --password your_password --database your_database
```

### Restore Command

```bash
python main.py restore <backup_file_name> --config-path config.yaml
```

Or provide details directly via CLI:

```bash
python main.py restore <backup_file_name> --db-type postgresql --host localhost --port 5432 --user your_user --password your_password --database your_database
```

## Example Commands

### 1. Backup Database (Using CLI Options)
```bash
python main.py backup --db-type mysql --host 127.0.0.1 --port 3306 --user root --password root_password --database my_database
```

### 2. Restore Database (Using Configuration File)
```bash
python main.py restore my_database_backup.sql --config-path config.yaml
```

## Roadmap

- [ ] Add encryption for backup files
- [ ] Support additional databases (e.g., MongoDB, Oracle)
- [ ] Integrate with Docker for easy deployment
- [ ] Add scheduling functionality

## Contributing

Contributions are welcome! Please open an issue to discuss your idea or submit a pull request.
