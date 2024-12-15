"""Env Settings."""

from pydantic_settings import BaseSettings


class EnvSettings(BaseSettings):
    """Class for environment."""

    TELEGRAM_BOT_TOKEN: str


env = EnvSettings()
