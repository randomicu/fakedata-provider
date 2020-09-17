from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.dialects.postgresql import ENUM

from app.db import metadata

event_table = Table(
    'event',
    metadata,
    Column('event_id', Integer, primary_key=True),
    Column('created_at', DateTime, nullable=False, default=func.now()),
    Column('language', String, nullable=False),
    Column('event_type', ENUM('address', 'person', name='event_type'), nullable=False)
)
