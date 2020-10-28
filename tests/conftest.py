#!/usr/bin/env python
import os
import pathlib

import pytest
from starlette.testclient import TestClient
from yoyo import get_backend
from yoyo import read_migrations

from app.main import app


# TODO: add settings override or add configuration app for ci environment
def get_test_database():
    if os.environ.get('CI'):
        return os.getenv('FAKEDATA_DATABASE_URL')
    else:
        return os.getenv('FAKEDATA_TEST_DATABASE_URL')


TEST_DATABASE_URL = get_test_database()


@pytest.fixture(scope='session')
def client() -> TestClient:
    yield TestClient(app)


@pytest.fixture(scope='session', autouse=True)
def setup_test_db():
    # backend = get_backend(TEST_DATABASE_URL)
    # migrations = read_migrations(str(pathlib.Path.cwd() / 'database' / 'sql'))
    #
    # with backend.lock():
    #     backend.apply_migrations(backend.to_apply(migrations))

    yield TEST_DATABASE_URL
