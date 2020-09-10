#!/usr/bin/env python

from requests import Response

from app.providers.address import get_country_code

EN_LOCALE_COUNTRY_CODE = "us"
RU_LOCALE_COUNTRY_CODE = "ru"


def test_address_router(client):
    response: Response = client.get("/v1/en/address")
    assert response.status_code == 200
    assert response.json()["address"]
    assert response.json()["calling_code"]
    assert response.json()["city"]
    assert response.json()["continent"]
    assert response.json()["coordinates"]
    assert response.json()["country"]
    assert response.json()["country_code"] == get_country_code(language="en") == EN_LOCALE_COUNTRY_CODE
    assert response.json()["latitude"]
    assert response.json()["longitude"]
    assert response.json()["postal_code"]
    assert response.json()["state"]
    assert response.json()["street_name"]
    assert response.json()["street_number"]
    assert response.json()["street_suffix"]
    assert response.json()["zip_code"]


def test_incorrect_locale(client):
    response: Response = client.get("/v1/unknown/address")
    assert response.status_code == 400


def test_inexistent_route(client):
    response: Response = client.get("/v1/en/no_route")
    assert response.status_code == 404
