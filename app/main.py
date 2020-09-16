#!/usr/bin/env python
from fastapi import FastAPI

from app.db import database
from app.routers import address
from app.routers import person

app = FastAPI()


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


app.include_router(address.router, prefix='/v1')
app.include_router(person.router, prefix='/v1')
