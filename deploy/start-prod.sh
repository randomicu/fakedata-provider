#!/usr/bin/env bash

sleep 5
yoyo apply -vvv --batch --database "$FAKEDATA_DATABASE_URL"

gunicorn -k uvicorn.workers.UvicornWorker -c gunicorn_conf.py app.main:app
