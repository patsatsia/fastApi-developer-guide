import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = 'FastAPI Developer Guide'
    DB_NAME: str = os.environ.get('DB_NAME')
    DB_USER: str = os.environ.get('DB_USER')
    DB_PASSWORD: str = os.environ.get('DB_PASSWORD')
    DB_PORT: int = os.environ.get('DB_PORT')
    DB_HOST: str = os.environ.get('DB_HOST')

    # PAGINATION SETTINGS
    PAGE_SIZE = 10


settings = Settings()
