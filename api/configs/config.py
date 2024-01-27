from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    #  App related
    APP_NAME: str = 'KiT'
    APP_DESCRIPTION: str = 'A'
    APP_VERSION: str = '0.1.0'


settings = Settings()
