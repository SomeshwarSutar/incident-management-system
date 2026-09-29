# SIMS API

SIMS is a FastAPI service for creating and retrieving incidents. It uses
SQLAlchemy with a local SQLite database and separates HTTP routing, business
logic, and persistence into distinct application layers.

## Features

- Create incidents with a title, description, and priority
- List all incidents
- Retrieve an incident by ID
- Check application health
- Interactive OpenAPI documentation

## Requirements

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/) for dependency and environment management

## Setup

Install the project dependencies from the repository root:

```powershell
uv sync
```

Start the API in development mode:

```powershell
uv run uvicorn app.main:app --reload
```

The service is available at `http://127.0.0.1:8000`. FastAPI provides
interactive documentation at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

The SQLite database is stored in `sims.db`. Its tables are created when the
application starts.

## API

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/health` | Return the application health status |
| `POST` | `/api/incidents/` | Create an incident |
| `GET` | `/api/incidents/` | List all incidents |
| `GET` | `/api/incidents/{incident_id}` | Retrieve an incident by ID |

### Health check

```powershell
curl.exe http://127.0.0.1:8000/health
```

Response:

```json
{
	"status": "ok"
}
```

### Create an incident

```powershell
curl.exe -X POST http://127.0.0.1:8000/api/incidents/ `
	-H "Content-Type: application/json" `
	-d '{"title":"Database unavailable","description":"Production database is not responding","priority":"high"}'
```

An incident response has the following shape:

```json
{
	"id": 1,
	"title": "Database unavailable",
	"description": "Production database is not responding",
	"priority": "high",
	"status": "open"
}
```

### List incidents

```powershell
curl.exe http://127.0.0.1:8000/api/incidents/
```

### Get an incident

```powershell
curl.exe http://127.0.0.1:8000/api/incidents/1
```

## Project structure

```text
app/
|-- main.py                          # Application setup and route registration
|-- api/
|   `-- incident.py                  # Incident HTTP endpoints
|-- core/
|   |-- config.py                    # Reserved for application configuration
|   `-- database.py                  # SQLAlchemy engine and sessions
|-- domain/
|   |-- models.py                    # SQLAlchemy models
|   `-- schemas.py                   # Pydantic request and response models
|-- repositories/
|   `-- incident_repository.py       # Incident persistence operations
`-- services/
		`-- incident_service.py          # Incident business logic
```

Requests flow through the application as follows:

```text
FastAPI route -> IncidentService -> IncidentRepository -> SQLite
```

## Current limitations

- Incident creation currently reads a `severity` attribute in the service,
	while the API schema and database model define `priority`. This mismatch must
	be corrected before the create endpoint can persist incidents.
- Missing incidents do not yet produce an explicit `404 Not Found` response.
- Update and delete operations are not implemented.
- Database schema migrations are not configured; tables are created directly
	from SQLAlchemy metadata at startup.
