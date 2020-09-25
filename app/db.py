#!/usr/bin/env python
from databases import Database
from sqlalchemy import create_engine
from sqlalchemy import MetaData

from app.config import get_app_settings


settings = get_app_settings()
DATABASE_URL = str(settings.database_url)


engine = create_engine(DATABASE_URL)
metadata = MetaData()


database = Database(DATABASE_URL)
