"""Runtime settings, read from environment variables (and .env for local runs)."""

from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    service_name: str = "fde-service"
    environment: str = "local"  # local | ci | dev | prod
    log_level: str = "INFO"

    # LLM provider selection. Providers and their base URLs live in config/providers.yaml.
    llm_provider: str = "mistral"
    llm_providers_file: str = "config/providers.yaml"
    llm_timeout_seconds: float = 30.0


@lru_cache
def get_settings() -> Settings:
    return Settings()
