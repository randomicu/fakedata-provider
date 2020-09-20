#!/usr/bin/env python
import pathlib

from pydantic import BaseSettings
from pydantic import PostgresDsn


class Settings(BaseSettings):
    database_url: PostgresDsn

    class Config:
        env_prefix = 'FAKEDATA_'
        env_file = str(pathlib.Path.cwd() / '.env')
