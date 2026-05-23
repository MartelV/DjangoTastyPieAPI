# Notable Django API

A full-stack Django + TastyPie note-taking app inspired by Google Keep.
Built with user authentication, per-user note management, and a REST API backend.

## Features
- User registration, login, and logout
- Notes are private per user
- Full CRUD via both web UI and REST API
- TastyPie REST API endpoints
- Admin dashboard

## REST API Endpoints
| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/v1/note/` | List all notes |
| GET | `/api/v1/note/<id>/` | Get a note |
| POST | `/api/v1/note/` | Create a note |
| PUT | `/api/v1/note/<id>/` | Update a note |
| DELETE | `/api/v1/note/<id>/` | Delete a note |

## Tech Stack
- Python 3.12
- Django 6.0
- django-tastypie
- SQLite

## Setup
```bash
git clone https://github.com/MartelV/DjangoTastyPieAPI.git
cd DjangoTastyPieAPI
python -m venv env
source env/bin/activate  # Windows: .\env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Then visit http://127.0.0.1:8000
