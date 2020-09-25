#!/usr/bin/env python
import pathlib

import pytest
from sqlalchemy_utils import create_database
from sqlalchemy_utils import drop_database
from starlette.testclient import TestClient
from yoyo import get_backend
from yoyo import read_migrations

from app.config import Settings
from app.main import app


# noinspection PyTypeChecker
def get_test_database():
    return Settings(database_url='postgresql://postgres:password@database:5432/fakedata_test')


config = get_test_database()
DATABASE_URL = str(config.database_url)


@pytest.fixture(scope='session')
def client() -> TestClient:
    yield TestClient(app)


@pytest.fixture(scope='session', autouse=True)
def setup_test_db():
    try:
        create_database(DATABASE_URL)
        backend = get_backend(DATABASE_URL)
        migrations = read_migrations(str(pathlib.Path.cwd() / 'database' / 'sql'))

        with backend.lock():
            backend.apply_migrations(backend.to_apply(migrations))

        yield DATABASE_URL
    finally:
        drop_database(DATABASE_URL)
