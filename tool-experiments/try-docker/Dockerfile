FROM python:3

ARG MY_ENV

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.0.0

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /usr/src/app

COPY poetry.lock pyproject.toml /usr/src/app/

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$MY_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY . /usr/src/app


