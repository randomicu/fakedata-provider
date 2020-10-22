#!/usr/bin/env python
from typing import Optional

from pydantic import BaseModel


class PersonSchema(BaseModel):
    age: int
    email: str
    first_name: str
    full_name: str
    gender: str
    height: str
    identifier: str
    last_name: str
    nationality: str
    occupation: str
    password: str
    political_views: str
    telephone: str
    title: str
    university: str
    username: str
    weight: int
    work_experience: int
    patronymic: Optional[str] = None
    inn: Optional[str] = None
    kpp: Optional[str] = None
    bic: Optional[str] = None
    ogrn: Optional[str] = None
    passport: Optional[str] = None
