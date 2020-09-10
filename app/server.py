#!/usr/bin/env python

import uvicorn

# noinspection PyUnresolvedReferences
from app.main import app

if __name__ == "__main__":
    uvicorn.run('server:app', host="0.0.0.0", port=8000, workers=1, reload=True)
