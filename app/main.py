#!/usr/bin/env python
from fastapi import FastAPI

from app.routers import address
from app.routers import person

app = FastAPI()
app.include_router(address.router, prefix='/v1')
app.include_router(person.router, prefix='/v1')
