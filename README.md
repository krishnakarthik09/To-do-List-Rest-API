# Flask To-Do List REST API

A lightweight, fully functional REST API built from scratch with Flask — no database, no boilerplate frameworks, just clean Python and the core mechanics of how real APIs work. Tasks are stored in memory and support full CRUD: **Create, Read, Update, and Delete.**

This project was built to demonstrate practical, hands-on understanding of Flask fundamentals: routing, dynamic URL parameters, JSON request/response handling, and correct HTTP status codes — the same patterns used in production-grade APIs.

## Features

- Full CRUD support (Create, Read, Update, Delete)
- Clean JSON responses for every endpoint
- Proper HTTP status codes (`200`, `201`, `404`) instead of generic success/failure
- Zero external dependencies beyond Flask
- Easy to test with `curl` or PowerShell's `Invoke-RestMethod`

## Tech Stack

- **Python 3**
- **Flask** — micro web framework

## Setup

```bash
pip install flask
python app.py
```

Server runs at:
```
http://127.0.0.1:5000
```

## Data Model

Each task is a simple JSON object:

```json
{
  "id": 1,
  "title": "Learn Flask",
  "done": false
}
```

## API Reference

| Method | Endpoint | Description |
|--------|----------|--------------|
| `GET` | `/tasks` | Get all tasks |
| `GET` | `/tasks/<id>` | Get a single task by ID |
| `POST` | `/tasks` | Create a new task |
| `PUT` | `/tasks/<id>` | Update an existing task |
| `DELETE` | `/tasks/<id>` | Delete a task by ID |

---

### `GET /tasks`
Returns every task currently stored.

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/tasks
```

**Response — `200 OK`**
```json
[
  { "id": 1, "title": "Learn Flask", "done": false },
  { "id": 2, "title": "Build API", "done": false }
]
```

---

### `GET /tasks/<id>`
Returns a single task matching the given ID.

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/tasks/1
```

**Response — `200 OK`**
```json
{ "id": 1, "title": "Learn Flask", "done": false }
```

**If the ID doesn't exist — `404 Not Found`**
```json
{ "error": "Task not found" }
```

---

### `POST /tasks`
Creates a new task. The ID is generated automatically.

**Body (JSON):**
```json
{ "title": "Test Task", "done": false }
```

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/tasks -Method POST -ContentType "application/json" -Body '{"title": "Test Task", "done": false}'
```

**Response — `201 Created`**
```json
{ "status": "success" }
```

---

### `PUT /tasks/<id>`
Updates the title and completion status of an existing task.

**Body (JSON):**
```json
{ "title": "Learn Flask deeply", "done": true }
```

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/tasks/1 -Method PUT -ContentType "application/json" -Body '{"title": "Learn Flask deeply", "done": true}'
```

**Response — `200 OK`**
```json
{ "status": "success" }
```

**If the ID doesn't exist — `404 Not Found`**
```json
{ "error": "Task not found" }
```

---

### `DELETE /tasks/<id>`
Permanently removes a task by ID.

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/tasks/3 -Method DELETE
```

**Response — `200 OK`**
```json
{ "status": "success" }
```

**If the ID doesn't exist — `404 Not Found`**
```json
{ "error": "Task not found" }
```

## Design Notes

- **In-memory storage**: tasks reset to the default list whenever the server restarts. This was a deliberate choice to focus purely on Flask's request/response cycle without database complexity getting in the way.
- **HTTP status codes are intentional, not decorative**: `201` is used only when a new resource is actually created, `200` for successful reads/updates/deletes, and `404` whenever a requested resource doesn't exist — matching real-world API conventions.
- **No frontend**: this is a pure backend API, designed to be consumed by any client (browser, curl, Postman, another app, etc).

## Possible Next Steps

- Swap the in-memory list for a real database (SQLite via SQLAlchemy)
- Add input validation (e.g. reject a `POST` with no `title`)
- Add pagination for `GET /tasks`
- Containerize with Docker for deployment
