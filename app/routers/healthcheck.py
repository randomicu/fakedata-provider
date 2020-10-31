#!/usr/bin/env python
from fastapi import APIRouter

from app.models.schema.healthcheck import HealthcheckSchema

router = APIRouter()


@router.get('/healthcheck')
async def get_status():
    data = {'status': 'UP'}

    return HealthcheckSchema(**data)
