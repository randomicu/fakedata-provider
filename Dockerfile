FROM python:3.8.5-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /usr/src/randomicu-fakedata

WORKDIR /usr/src/randomicu-fakedata

COPY . /usr/src/randomicu-fakedata
COPY ./deploy /usr/src/randomicu-fakedata

RUN set -eux && \
    apt-get update && \
    apt-get install --yes --no-install-recommends curl && \
    apt-get clean autoclean && \
    apt-get autoremove --yes && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/ && \
    rm -rf /var/lib/apt/lists/* && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false && \
    cd /usr/src/randomicu-fakedata && \
    poetry install --no-root

CMD ["/usr/src/randomicu-fakedata/start.sh"]
