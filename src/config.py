from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import os

# user = os.environ.get('DB_USER')
# password = os.environ.get('DB_PASSWORD')
# host = os.environ.get('DB_HOST')
# port = os.environ.get('DB_PORT')
# schema = os.environ.get('DB_SCHEMA')

# def get_mysql_uri():
#     return f"mysql+pymysql://{user}:{password}@{host}:{port}/{schema}?charset=utf8mb4"

def get_sqlite_uri():
    return "sqlite:///./sqlite.db"

Base = declarative_base()
DB_URL = get_sqlite_uri()