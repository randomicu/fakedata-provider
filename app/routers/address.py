#!/usr/bin/env python

from fastapi import Depends, APIRouter
from mimesis import Address

from app.middlewares import verify_mimesis_locales
from app.models.address import AddressSchema
from app.providers.address import get_country_code

router = APIRouter()


@router.get("/{lang}/address", dependencies=[Depends(verify_mimesis_locales)])
async def get_address(lang: str):
    address: Address = Address(lang)

    schema = AddressSchema(
        address=address.address(),
        calling_code=address.calling_code(),
        city=address.city(),
        continent=address.continent(),
        coordinates=address.coordinates(),
        country=address.country(),
        country_code=get_country_code(lang),
        latitude=address.latitude(),
        longitude=address.longitude(),
        postal_code=address.postal_code(),
        state=address.state(),
        street_name=address.street_name(),
        street_number=address.street_number(),
        street_suffix=address.street_suffix(),
        zip_code=address.zip_code())

    return schema
