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
