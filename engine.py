import os
import sys
import sqlalchemy
from configparser import ConfigParser

APP_PATH = str(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(APP_PATH)


# Import database configuration from file
config = ConfigParser()
config.read(f"{APP_PATH}/database.conf")

# If environment variables are present, override config file
if "db_credential" not in config:
    config["db_credential"] = {}
if "DB_USER" in os.environ:
    config["db_credential"]["user"] = os.environ.get("DB_USER")
if "DB_PASSWORD" in os.environ:
    config["db_credential"]["password"] = os.environ.get("DB_PASSWORD")
if "DB_HOST" in os.environ:
    config["db_credential"]["host"] = os.environ.get("DB_HOST")
if "DB_PORT" in os.environ:
    config["db_credential"]["port"] = os.environ.get("DB_PORT")
if "DB_NAME" in os.environ:
    config["db_credential"]["database"] = os.environ.get("DB_NAME")

# Set up and establish database engine
# URL format: postgresql://<username>:<password>@<hostname>:<port>/<database>
DATABASE_URL = f"postgresql+psycopg2://{config['db_credential']['user']}:{config['db_credential']['password']}@{config['db_credential']['host']}:{config['db_credential']['port']}/{config['db_credential']['database']}"
engine = sqlalchemy.create_engine(DATABASE_URL)


def get_engine():
    return engine
