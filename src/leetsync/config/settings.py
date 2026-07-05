"""
Configuration management for LeetSync.
"""

try:
    from pydantic_settings import BaseSettings, SettingsConfigDict
except Exception as exc:
    raise RuntimeError(
        "Missing dependency: install 'pydantic-settings' (and 'pydantic' >=2).\n"
        "Run: pip install pydantic pydantic-settings"
    ) from exc
from typing import Optional


class Settings(BaseSettings):
    """Application configuration."""

    leetcode_username: str

    repository_path: str

    poll_interval: int = 5

    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


_settings: Optional[Settings] = None


def get_settings() -> Settings:
    """Return a cached `Settings` instance, creating it lazily.

    This avoids validating required environment variables at import time
    (which raised `ValidationError` previously). Call this from application
    entrypoints when configuration is actually needed.
    """
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings