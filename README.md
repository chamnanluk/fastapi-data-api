# FastAPI Data API Starter Project

A beginner-friendly but production-shaped FastAPI starter project for a Junior Data Engineer.

## What this project includes

- FastAPI app with modular routes
- PostgreSQL connection using SQLAlchemy
- DuckDB analytics endpoint
- Pydantic request/response schemas
- Dependency Injection for DB sessions
- Middleware for request timing
- Background task for audit logging
- Sample SQL and DuckDB seed script

## Project structure

```text
fastapi-data-api/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes/
│   │       ├── health.py
│   │       ├── jobs.py
│   │       ├── metrics.py
│   │       ├── orders.py
│   │       └── sales.py
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   ├── schemas/
│   │   ├── jobs.py
│   │   ├── metrics.py
│   │   ├── orders.py
│   │   └── sales.py
│   └── services/
│       ├── duckdb_service.py
│       ├── job_service.py
│       └── postgres_service.py
├── scripts/
│   ├── init_duckdb.py
│   └── init_postgres.sql
├── analytics.duckdb
├── requirements.txt
└── .env.example
```

## 1. Create virtual environment

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS/Linux
```bash
python -m venv .venv
source .venv/bin/activate
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Create your environment file

Copy `.env.example` to `.env`

### Windows
```bash
copy .env.example .env
```

### macOS/Linux
```bash
cp .env.example .env
```

## 4. Prepare PostgreSQL

Create a database named `salesdb`, then run:

```bash
psql -U postgres -d salesdb -f scripts/init_postgres.sql
```

If `psql` is not in your PATH, open pgAdmin or your SQL tool and run the SQL file manually.

## 5. Prepare DuckDB

Run:

```bash
python scripts/init_duckdb.py
```

This creates and seeds `analytics.duckdb`.

## 6. Start the API

```bash
uvicorn app.main:app --reload
```

Open:
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## Endpoints

### Health
- `GET /`
- `GET /health`
- `GET /health/db`

### Orders
- `GET /orders?limit=10`

### Metrics
- `GET /metrics/top-products?limit=5`
- `GET /metrics/by-region?region=Phnom Penh`

### Sales
- `POST /sales/query`

### Jobs
- `POST /refresh-report`

## Example request body for `/sales/query`

```json
{
  "country": "Cambodia",
  "year": 2025,
  "product": "Rice"
}
```

## What to practice next

- add tests with pytest
- add async database support
- add Docker
- add pagination metadata
- add logging to a proper logger instead of a text file
- add auth
