import os
import sys
from contextlib import contextmanager

import sqlalchemy

APP_PATH = str(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(APP_PATH)

config = {}
config["db_credential"] = {}
config["db_credential"]["user"] = os.environ["DB_USER"]
config["db_credential"]["password"] = os.environ["DB_PASSWORD"]
config["db_credential"]["host"] = os.environ["DB_HOST"]
config["db_credential"]["port"] = os.environ["DB_PORT"]
config["db_credential"]["database"] = os.environ["DB_NAME"]

# Set up and establish database engine
# URL format: postgresql://<username>:<password>@<hostname>:<port>/<database>
DATABASE_URL = f"postgresql+psycopg2://{config['db_credential']['user']}:{config['db_credential']['password']}@{config['db_credential']['host']}:{config['db_credential']['port']}/{config['db_credential']['database']}"

engine = sqlalchemy.create_engine(DATABASE_URL)  # type: sqlalchemy.engine.Engine


@contextmanager
def get_connection() -> sqlalchemy.engine.Connection:
    connection = engine.connect()
    try:
        yield connection
    finally:
        connection.close()
