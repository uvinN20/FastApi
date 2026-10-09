# FastAPI Product Management API

A FastAPI application for managing a product catalog stored in MySQL. The API supports listing, retrieving, adding, updating, and deleting products.

## Features

- List all products
- Retrieve a single product by ID
- Add a new product
- Update an existing product
- MySQL-backed product storage
- Automatic creation of the products table
- Sample products inserted when the products table is first created
- Automatic request validation using Pydantic models

## Run locally

1. Start the MySQL service and create the `fastapi_db` database, or update the connection URL in `database.py` to use another database.
2. Install the dependencies in your virtual environment: `fastapi`, `uvicorn`, `sqlalchemy`, and `pymysql`.
3. Start the API with `uvicorn main:app --reload`.

The application creates the `products` table at startup. The initial sample products are inserted only when that table is created for the first time.

## Project Structure

```text
.
├── .gitignore
├── main.py
├── models.py
└── README.md
