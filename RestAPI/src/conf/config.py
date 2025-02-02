from typing import Any

from pydantic import ConfigDict, field_validator, EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = "postgresql+asyncpg://postgres:qazxsw123456@localhost:5432/contactsbase"
    SECRET_KEY_JWT: str = "1234567890"
    ALGORITHM: str = "HS256"
    MAIL_USERNAME: EmailStr = "postgres@email.com"
    MAIL_PASSWORD: str = "postgres"
    MAIL_FROM: str = "postgres@email.com"
    MAIL_PORT: int = 567234
    MAIL_SERVER: str = "postgres"
    REDIS_DOMAIN: str = 'localhost'
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str | None = None
    CLOUDINARY_NAME: str = "cloud"
    CLOUDINARY_API_KEY: int = 1234567
    CLOUDINARY_API_SECRET: str = 'secret'


    @field_validator('ALGORITHM')
    @classmethod
    def validate_algorithm(cls, value: Any):
        if value not in ["HS256", "HS512"]:
            raise ValueError("ALGORITHM must be HS256 or HS512")
        return value

    model_config = ConfigDict(extra='ignore', env_file = ".env", env_file_encoding = "utf-8") # noqa


config = Settings()
