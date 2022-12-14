# Simple CRUD REST API

Simple CRUD API to process Receipt resources

## Running application

### Simple Python

1. `pip install -r requirements.txt`
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. `python manage.py runserver`

### Docker

1. `docker-compose up`

## Endpoints

All endpoints are available at:

- `127.0.0.1:8000/schema/swagger-ui/` - Swagger UI
- `127.0.0.1:8000/schema/` - Swagger file

`PUT` and `PATCH` are not implemented properly, per assignment tasks, hence throwing 500 error

## Running endpoints

### Swagger UI

- Running through Swagger UI `127.0.0.1:8000/schema/swagger-ui/`

### Postman

- Importing `postman_collection.json` and running endpoints from Postman

## Tech stack

- Language: **Python**
- Framework: **Django REST framework**
- DB: **SQLite**
- Additional libraries:
  - **drf-spectacular**: Swagger generation
  - **django-filter**: Query filtering
