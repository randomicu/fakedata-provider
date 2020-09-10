#!/usr/bin/env python

# This module is wrapper for Mimesis's gender provider
from mimesis.enums import Gender


def get_person_gender(gender: str) -> Gender:
    # if lang == en, gender could be: male, female, fluid, other
    # if lang == ru, gender could be: Муж., Жен.

    return Gender.MALE if gender == 'Male' else Gender.FEMALE
