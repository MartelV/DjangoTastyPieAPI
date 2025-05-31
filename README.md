# Notable Django API

A Django + TastyPie REST API for managing notes, inspired by Google Keep.  
Implements full CRUD functionality with model-backed endpoints, tested via Postman.

## Features

- Django ORM for data modeling
- TastyPie for RESTful API endpoints
- Fully working CRUD: Create, Read, Update, Delete
- Postman tested
- Admin dashboard enabled

## Endpoints

| Method | URL                      | Description              |
|--------|--------------------------|--------------------------|
| GET    | `/api/note/`             | List all notes           |
| GET    | `/api/note/<id>/`        | Retrieve a specific note |
| POST   | `/api/note/`             | Create a new note        |
| PUT    | `/api/note/<id>/`        | Update a note            |
| DELETE | `/api/note/<id>/`        | Delete a note            |

## Example JSON

```json
{
  "title": "First Note",
  "body": "This is certainly noteworthy"
}
```

## Requirements

- Python 3.10+
- Django 5.2.1
- django-tastypie

Install all dependencies with:

```bash
pip install -r requirements.txt
```

## Setup Instructions

## Clone the Repo
```
git clone https://github.com/MartelV/DjangoTastyPieAPI.git
cd DjangoTastyPieAPI
```
## Set Up Virtual Environment
```
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
```
## Install Requirements
```
pip install -r requirements.txt
```
## Apply Migrations
```
python manage.py migrate
```

## (Optional) Create Admin User
```
python manage.py createsuperuser
```
## Run the Server
```
python manage.py runserver
```
Then visit:
http://127.0.0.1:8000/api/note/

---
