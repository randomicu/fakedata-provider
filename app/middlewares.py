#!/usr/bin/env python
from fastapi import HTTPException
from starlette.requests import Request

from .providers.address import MIMESIS_LANGUAGES


async def verify_mimesis_locales(request: Request):
    """
    Used as middleware for all requests to check if requested url path is in allowed set

    :param request: Starlette.requests.Request object
    """
    if (request.path_params['lang']
            and request.path_params['lang']) not in MIMESIS_LANGUAGES.keys():

        raise HTTPException(status_code=400, detail='Incorrect locale')
