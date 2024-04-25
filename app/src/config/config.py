from os import getenv
from dotenv import load_dotenv
load_dotenv()

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    #DATABASE
    MYSQL_USER:str=getenv("MYSQL_USER")
    MYSQL_PASSWORD:str=getenv("MYSQL_PASSWORD")
    MYSQL_HOST:str=getenv("MYSQL_HOST")
    MYSQL_DATABASE:str=getenv("MYSQL_DATABASE")
    MYSQL_PORT:str=getenv("MYSQL_PORT")
    
    # API-KEY
    API_KEY: str = getenv("API_KEY")
    class Config:
        case_sensitive = True

settings = Settings()