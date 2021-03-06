#!/usr/bin/env python
from requests import Response


def test_en_person_router(client):
    with client:
        response: Response = client.get('/v1/en/person')

    response_structure = {
        'age': '',
        'email': '',
        'first_name': '',
        'full_name': '',
        'gender': '',
        'height': '',
        'identifier': '',
        'last_name': '',
        'nationality': '',
        'occupation': '',
        'password': '',
        'political_views': '',
        'telephone': '',
        'title': '',
        'university': '',
        'username': '',
        'weight': '',
        'work_experience': ''
    }

    assert response.status_code == 200
    assert response_structure.keys() == response.json().keys()


def test_ru_person_router(client):
    with client:
        response: Response = client.get('/v1/ru/person')
    response_structure = {
        'age': '',
        'email': '',
        'first_name': '',
        'full_name': '',
        'gender': '',
        'height': '',
        'identifier': '',
        'last_name': '',
        'nationality': '',
        'occupation': '',
        'password': '',
        'political_views': '',
        'telephone': '',
        'title': '',
        'university': '',
        'username': '',
        'weight': '',
        'work_experience': '',
        'patronymic': '',
        'inn': '',
        'kpp': '',
        'bic': '',
        'ogrn': '',
        'passport': ''
    }

    assert response.status_code == 200
    assert response_structure.keys() == response.json().keys()


def test_incorrect_locale(client):
    with client:
        response: Response = client.get('/v1/unknown/person')
    assert response.status_code == 400
