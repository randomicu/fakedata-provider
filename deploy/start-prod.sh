#!/usr/bin/env bash

sleep 5

gunicorn -k uvicorn.workers.UvicornWorker -c gunicorn_conf.py app.main:app
