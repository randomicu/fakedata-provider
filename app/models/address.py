#!/usr/bin/env python

from typing import Union

from pydantic import BaseModel


class AddressSchema(BaseModel):
    address: str
    calling_code: str
    city: str
    continent: str
    coordinates: dict
    country: str
    country_code: str
    latitude: Union[str, float]
    longitude: Union[str, float]
    postal_code: str
    state: str
    street_name: str
    street_number: str
    street_suffix: str
    zip_code: str
