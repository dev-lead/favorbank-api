# favorbank-api
A Platform for Kindness and Community

## Create and Activate virtual environment
`python -m venv .venv`

## Sync your environment directly with pyproject.toml
uv pip sync pyproject.toml

## Application structure
favorbank-api/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── users.py
│   │   │   │   └── items.py
│   │   │   └── router.py
│   ├── core/
│   │   ├── config.py         # Pydantic BaseSettings for env vars
│   │   └── database.py       # Async engine & sessionmaker
│   ├── models/               # ORM Models (SQLAlchemy / SQLModel)
│   ├── schemas/              # Data Validation (Pydantic Models)
│   ├── services/             # Business Logic Layer
│   └── main.py               # FastAPI App instance creation
├── tests/
├── .env.example
├── .pythin-version
└── pyproject.toml

## Run the server
### As a package
uv run uvicorn app.main:app --reload --port 8000
### Run directly
uv run --no-build-isolation --no-project uvicorn app.main:app --reload --port 8000