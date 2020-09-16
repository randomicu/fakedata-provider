#!/usr/local/bin python
from fastapi import APIRouter
from fastapi import Depends
from mimesis import Person

from app.helpers.send_event import send_event
from app.middlewares import verify_mimesis_locales
from app.models.schema.person import PersonSchema
from app.providers.person import get_additional_data
from app.providers.person import get_data
from app.providers.person import get_person_gender

router = APIRouter()


@router.get('/{lang}/person',
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

    await send_event(event_type='person', language=lang)

    return PersonSchema(**data)
