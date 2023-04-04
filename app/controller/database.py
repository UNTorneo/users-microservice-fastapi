from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DB_NAME = os.environ.get('DB_NAME') or 'fastapi_db'
DB_USER = os.environ.get('DB_USER') or 'fastapi'
DB_PASSWORD = os.environ.get('DB_PASSWORD') or '123'
DB_HOST = os.environ.get('DB_HOST') or 'localhost'
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()