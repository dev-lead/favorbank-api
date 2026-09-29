from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = ""
    ENVIRONMENT: str = ""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

# lru_cache ensures the .env file is read only once
@lru_cache
def get_settings() -> Settings:
    return Settings()