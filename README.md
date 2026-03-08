# project-api-testing

A Django API that exposes an endpoint for listing books in a library.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install django
```

## Run

```bash
python manage.py runserver
```

## Endpoint

- `GET /list`: returns 100 books from an in-code data source.
