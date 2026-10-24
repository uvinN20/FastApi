# FastAPI Product API

A Python REST API for a MySQL product catalogue, using **FastAPI**, **Pydantic** and **SQLAlchemy**.

## API routes

| Method | Route | Purpose |
| --- | --- | --- |
| GET | `/` | Welcome message |
| GET | `/products` | List products |
| GET | `/product/{id}` | Retrieve a product |
| POST | `/product` | Create a product |
| PUT | `/product/{id}` | Update a product |
| DELETE | `/product/{id}` | Delete a product |

## Run locally

1. Create and activate a Python virtual environment. Use Python 3.10 or newer.
2. Install dependencies:

   ```bash
   python -m pip install fastapi uvicorn sqlalchemy pymysql
   ```

3. Start MySQL, create the `fastapi_db` database and configure the connection in `database.py` for your local environment.
4. Start the API:

   ```bash
   python -m uvicorn main:app --reload
   ```

Open **http://127.0.0.1:8000/docs** to explore the generated API documentation.

The application creates the products table at startup and inserts sample products only when the table is first created.

## Source guide

| File | Responsibility |
| --- | --- |
| [main.py](main.py) | Routes and startup initialization |
| [models.py](models.py) | Pydantic product schema |
| [database_model.py](database_model.py) | SQLAlchemy table model |
| [database.py](database.py) | Database engine and session lifecycle |

## Current limitations

This is a learning project. It has no authentication, and missing-product responses currently return messages rather than HTTP 404 errors. Dependency versions are not pinned.

Database configuration is currently embedded in source. Move it to environment variables before sharing deployment configuration, and replace any real credentials that have been committed.
