#!/usr/bin/env python
from databases import Database
from sqlalchemy import create_engine
from sqlalchemy import MetaData

from app.config import Settings

settings = Settings()
DATABASE_URL = str(settings.database_url)


engine = create_engine(DATABASE_URL)
metadata = MetaData()


database = Database(DATABASE_URL)
