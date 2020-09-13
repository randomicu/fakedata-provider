#!/usr/bin/env python
# This module is wrapper for Mimesis's gender provider
from mimesis import Person
from mimesis.builtins import RussiaSpecProvider
from mimesis.enums import Gender


def get_data(person: Person, gender):
    return {
        'gender': str(gender.value).capitalize(),
        'academic_degree': person.academic_degree(),
        'age': person.age(),
        'avatar': person.avatar(),
        'blood_type': person.blood_type(),
        'email': person.email(),
        'name': person.name(gender=gender),
        'surname': person.surname(gender=gender),
        'first_name': person.first_name(gender=gender),
        'last_name': person.last_name(gender=gender),
        'full_name': person.full_name(gender=gender),
        'height': person.height(),
        'identifier': person.identifier(),
        'language': person.language(),
        'person_name': person.name(gender=gender),
        'nationality': person.nationality(gender=gender),
        'occupation': person.occupation(),
        'password': person.password(),
        'political_views': person.political_views(),
        'sexual_orientation': person.sexual_orientation(),
        'social_media_profile': person.social_media_profile(),
        'telephone': person.telephone(),
        'title': person.title(gender=gender),
        'university': person.university(),
        'username': person.username(),
        'views_on': person.views_on(),
        'weight': person.weight(),
        'work_experience': person.work_experience(),
        'worldview': person.worldview()
    }


def get_additional_data(lang: str, gender):
    if lang == 'ru':
        ru = RussiaSpecProvider()
        additional_data = {
            'patronymic': ru.patronymic(gender=gender),
            'inn': ru.inn(),
            'kpp': ru.kpp(),
            'bic': ru.bic(),
            'ogrn': ru.ogrn(),
            'passport': ru.series_and_number()
        }

        return additional_data


def get_person_gender(gender_code: int) -> Gender:
    """
    :param gender_code:
        Codes for the representation of human sexes is an international
        standard (0 - not known, 1 - male, 2 - female, 9 - not applicable).
    """

    if gender_code == 0:
        return Gender.MALE
    elif gender_code == 1:
        return Gender.MALE
    elif gender_code == 2:
        return Gender.FEMALE
    else:
        return Gender.FEMALE
