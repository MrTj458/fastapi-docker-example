import os
from functools import lru_cache
from pydantic import BaseSettings, AnyUrl

class Settings(BaseSettings):
    database_url: AnyUrl = os.getenv('DATABASE_URL')
    page_length: int = 10

@lru_cache()
def get_settings():
    return Settings()
