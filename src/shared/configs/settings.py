from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.shared.configs.app_config import AppConfig


class Settings(BaseSettings):
    app_config: AppConfig = AppConfig()

    DATABASE_URL: Optional[str] = None
    JWT_SECRET_KEY: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
