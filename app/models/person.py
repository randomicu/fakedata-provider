#!/usr/bin/env python

from typing import Optional

from pydantic import BaseModel


class PersonSchema(BaseModel):
    academic_degree: str
    age: int
    avatar: str
    blood_type: str
    email: str
    first_name: str
    full_name: str
    gender: str
    height: str
    identifier: str
    language: str
    last_name: str
    name: str
    nationality: str
    occupation: str
    password: str
    political_views: str
    sexual_orientation: str
    social_media_profile: str
    surname: str
    telephone: str
    title: str
    university: str
    username: str
    views_on: str
    weight: int
    work_experience: int
    worldview: str
    patronymic: Optional[str] = None
    inn: Optional[str] = None
    kpp: Optional[str] = None
    bic: Optional[str] = None
    ogrn: Optional[str] = None
    passport: Optional[str] = None
