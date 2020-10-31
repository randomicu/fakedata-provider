#!/usr/bin/env python
from pydantic import BaseModel


class HealthcheckSchema(BaseModel):
    status: str
