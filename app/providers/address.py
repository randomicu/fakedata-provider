#!/usr/bin/env python

# This module is wrapper for Mimesis's address provider


# Map Mimesis languages like "locale": "country_code"
MIMESIS_LANGUAGES = {
    "en": "us",
    "ru": "ru"
}


def get_country_code(language: str) -> str:
    return MIMESIS_LANGUAGES[language]
