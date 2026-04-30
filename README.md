# fastapi-notes-api

A production-structured REST API for managing notes, built with FastAPI and SQLAlchemy.

## Tech Stack

- **FastAPI** — API framework
- **SQLAlchemy** — ORM for database operations
- **Pydantic** — request/response validation
- **SQLite** — lightweight SQL database
- **Uvicorn** — ASGI server


## Run

```bash
uvicorn app.main:app --reload --port 8000
```

API docs available at `http://localhost:8000/docs`

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/notes/` | Create a note |
| GET | `/notes/` | List all notes |
| GET | `/notes/{id}` | Get a single note |
| PUT | `/notes/{id}` | Update a note |
| DELETE | `/notes/{id}` | Delete a note |
| GET | `/health` | Health check |

## Key Concepts

- **Layered architecture** — config, database, models, schemas, and routes are fully separated
- **Dependency injection** — DB session lifecycle managed via FastAPI's `Depends()`
- **Pydantic validation** — all input validated before reaching business logic
- **Partial updates** — `PUT` only updates fields explicitly sent in the request
- **ORM** — no raw SQL anywhere, SQLAlchemy handles all database operations