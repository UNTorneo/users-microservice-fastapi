from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

dbName = os.environ.get('dbName') or 'fastapi_db'
dbUser = os.environ.get('dbUser') or 'fastapi'
dbPassword = os.environ.get('dbPassword') or '123'
dbHost = os.environ.get('dbHost') or 'localhost'
sqlalchemyDatabaseUrl = f"postgresql://{dbUser}:{dbPassword}@{dbHost}/{dbName}"

engine = create_engine(
    sqlalchemyDatabaseUrl
)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()