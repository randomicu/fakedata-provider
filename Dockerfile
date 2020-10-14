FROM ghcr.io/randomicu/fakedata-backend-base:1.0.0 as builder-dev

RUN set -eux && \
    apt-get install --yes --no-install-recommends build-essential

WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root --no-dev

# Development image
FROM ghcr.io/randomicu/fakedata-backend-base:1.0.0

WORKDIR $PYSETUP_PATH
COPY --from=builder-dev $POETRY_HOME $POETRY_HOME
RUN true
COPY --from=builder-dev $PYSETUP_PATH $PYSETUP_PATH

RUN poetry install --no-root

WORKDIR /usr/src/randomicu-fakedata

COPY . /usr/src/randomicu-fakedata
COPY ./deploy/start.sh /usr/src/randomicu-fakedata/start.sh

CMD ["/usr/src/randomicu-fakedata/start.sh"]
