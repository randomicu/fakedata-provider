import os

from databases import Database
from sqlalchemy import create_engine
from sqlalchemy import MetaData

DATABASE_URL = os.getenv('FAKEDATA_DATABASE_URL')


engine = create_engine(DATABASE_URL)
metadata = MetaData()


database = Database(DATABASE_URL)
