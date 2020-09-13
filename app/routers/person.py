#!/usr/local/bin python

from fastapi import APIRouter, Depends
from mimesis import Person

from app.middlewares import verify_mimesis_locales
from app.models.person import PersonSchema
from app.providers.person import get_person_gender, get_additional_data, get_data

router = APIRouter()


@router.get("/{lang}/person",
            dependencies=[Depends(verify_mimesis_locales)],
            response_model=PersonSchema,
            response_model_exclude_none=True)
async def get_person(lang: str):
    person: Person = Person(lang)
    person_gender = get_person_gender(person.gender(iso5218=True))
    data = get_data(person, person_gender)
    additional_data = get_additional_data(lang, person_gender)

    if additional_data:
        data.update(additional_data)

    return PersonSchema(**data)
