#!/usr/local/bin python

from fastapi import APIRouter, Depends
from mimesis import Person

from app.middlewares import verify_mimesis_locales
from app.models.person import PersonSchema
from app.providers.person import get_person_gender

router = APIRouter()


@router.get("/{lang}/person", dependencies=[Depends(verify_mimesis_locales)])
async def get_person(lang: str):
    person: Person = Person(lang)

    gender = person.gender()
    degree = person.academic_degree()
    age = person.age()
    avatar = person.avatar()
    blood_type = person.blood_type()
    email = person.email()
    name = person.first_name(gender=get_person_gender(gender))
    full_name = person.full_name(gender=get_person_gender(gender))
    height = person.height()
    identifier = person.identifier()
    language = person.language()
    last_name = person.last_name(gender=get_person_gender(gender))
    person_name = person.name(gender=get_person_gender(gender))
    nationality = person.nationality(gender=get_person_gender(gender))
    occupation = person.occupation()
    password = person.password()
    political_views = person.political_views()
    sexual_orientation = person.sexual_orientation()
    social_media_profile = person.social_media_profile()
    surname = person.surname(gender=get_person_gender(gender))
    telephone = person.telephone()
    title = person.title(gender=get_person_gender(gender))
    university = person.university()
    username = person.username()
    views_on = person.views_on()
    weight = person.weight()
    experience = person.work_experience()
    worldview = person.worldview()

    schema = PersonSchema(
        academic_degree=degree,
        age=age,
        avatar=avatar,
        blood_type=blood_type,
        email=email,
        first_name=name,
        full_name=full_name,
        gender=gender,
        height=height,
        identifier=identifier,
        language=language,
        last_name=last_name,
        name=person_name,
        nationality=nationality,
        occupation=occupation,
        password=password,
        political_views=political_views,
        sexual_orientation=sexual_orientation,
        social_media_profile=social_media_profile,
        surname=surname,
        telephone=telephone,
        title=title,
        university=university,
        username=username,
        views_on=views_on,
        weight=weight,
        work_experience=experience,
        worldview=worldview,
    )

    return schema
