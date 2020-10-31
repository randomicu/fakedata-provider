#!/usr/bin/env python
from requests import Response


def test_healthcheck_router(client):
    with client:
        response: Response = client.get('/healthcheck')

    response_structure = {
        'status': 'UP'
    }

    assert response.status_code == 200
    assert response_structure.keys() == response.json().keys()
    assert response_structure == response.json()
