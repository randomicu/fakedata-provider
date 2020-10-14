#!/bin/bash

sleep 5
yoyo apply -vvv --batch --database "$FAKEDATA_DATABASE_URL"

uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
