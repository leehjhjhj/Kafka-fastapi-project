from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

# user = os.environ.get('DB_USER')
# password = os.environ.get('DB_PASSWORD')
# host = os.environ.get('DB_HOST')
# port = os.environ.get('DB_PORT')
# schema = os.environ.get('DB_SCHEMA')

# def get_mysql_uri():
#     return f"mysql+pymysql://{user}:{password}@{host}:{port}/{schema}?charse

def get_sqlite_uri():
    return "sqlite:///./sqlite.db"

Base = declarative_base()
DB_URL = get_sqlite_uri()
engine = create_async_engine(DB_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session