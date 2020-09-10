#!/usr/bin/env python

from requests import Response


def test_person_router(client):
    response: Response = client.get("/v1/en/person")
    assert response.status_code == 200
    assert response.json()["academic_degree"]
    assert response.json()["age"]
    assert response.json()["avatar"]
    assert response.json()["blood_type"]
    assert response.json()["email"]
    assert response.json()["first_name"]
    assert response.json()["full_name"]
    assert response.json()["gender"]
    assert response.json()["height"]
    assert response.json()["identifier"]
    assert response.json()["language"]
    assert response.json()["last_name"]
    assert response.json()["name"]
    assert response.json()["nationality"]
    assert response.json()["occupation"]
    assert response.json()["password"]
    assert response.json()["political_views"]
    assert response.json()["sexual_orientation"]
    assert response.json()["social_media_profile"]
    assert response.json()["surname"]
    assert response.json()["telephone"]
    assert response.json()["title"]
    assert response.json()["university"]
    assert response.json()["username"]
    assert response.json()["views_on"]
    assert response.json()["weight"]
    assert response.json()["worldview"]
    assert "work_experience" in response.json()


def test_incorrect_locale(client):
    response: Response = client.get("/v1/unknown/person")
    assert response.status_code == 400
