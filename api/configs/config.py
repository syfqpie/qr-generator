from pydantic import BaseSettings

class Settings(BaseSettings):
    #  App related
    APP_NAME: str = 'A'
    APP_DESCRIPTION: str = 'A'
    APP_VERSION: str = '0.0.1'
    TAGS_METADATA = [
        {
            "name": "users",
            "description": "Operations with users"
        }
    ]

    # Mail related
    EMAIL_SENDER: str = ''
    SMTP_SERVER: str = ''

    # Database related
    DATABASE_USER: str = ''
    DATABASE_PASSWORD: str = ''
    DATABASE_SERVER: str = ''
    DATABASE_NAME: str = ''

settings = Settings()