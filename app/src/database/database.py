import logging

from app.src.config.config import settings

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker

logger = logging.getLogger()

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}@mysql:{settings.MYSQL_PORT}/{settings.MYSQL_DATABASE}?charset=utf8mb4'

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
if not database_exists(engine.url):
    create_database(engine.url)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    database=session_local()
    try:
        yield database
    finally:
        database.close()