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

Requirements
Python 3.10+

Django 5.2.1

django-tastypie

Install all dependencies with:

bash
Copy
Edit
pip install -r requirements.txt

Setup Instructions
# Clone the repo
git clone https://github.com/MartelV/DjangoTastyPieAPI.git
cd DjangoTastyPieAPI

# Set up virtual environment
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# (Optional) Create admin user
python manage.py createsuperuser

# Run the server
python manage.py runserver

Then visit:
📍 http://127.0.0.1:8000/api/note/
