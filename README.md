# Randomicu-fakedata

random.icu companion service with internal API for data generation from Mimesis providers.

## Available providers

1. Address
2. Person

## Development

Run `uvicorn` in development mode on 8000 port (with autoreload) from repo root:

`PYTHONPATH=$(pwd) uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000`

## Deployment

Deploy notes.

## Testing

Run this command from repo root to run all tests:

`PYTHONPATH=$(pwd) pytest -s tests`
