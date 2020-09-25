#!/usr/bin/env python
from functools import lru_cache

from pydantic import BaseSettings
from pydantic import PostgresDsn


class Settings(BaseSettings):
    database_url: PostgresDsn

    class Config:
        env_prefix = 'FAKEDATA_'


@lru_cache
def get_app_settings() -> Settings:
    return Settings()
