# Use the official Node.js image from the Docker Hub
FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and change to the app directory
WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock ./


RUN pip install poetry




RUN poetry config virtualenvs.create false \
    && poetry lock --no-update && poetry install --only main --no-interaction --no-ansi

COPY . .
