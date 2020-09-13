#!/usr/bin/env python

from fastapi import Depends, APIRouter
from mimesis import Address

from app.middlewares import verify_mimesis_locales
from app.models.address import AddressSchema
from app.providers.address import get_data

router = APIRouter()


@router.get("/{lang}/address", dependencies=[Depends(verify_mimesis_locales)])
async def get_address(lang: str):
    address: Address = Address(lang)
    data = get_data(address, lang)

    return AddressSchema(**data)
