# pyrefly: ignore [missing-import]
from fastapi import FastAPI #this is the main.py file that contains the FastAPI application and defines the REST API endpoints for the product management system.
from models import Product

app = FastAPI()


@app.get("/")  # this REST API endpoint returns a greeting message
def greet():
    return "welcome to the program!"


products = [
    Product(
        id=1,
        name="phone",
        description="budget phone",
        price=99.0,
        quantity=10,
    ),
    Product(
        id=2,
        name="laptop",
        description="gaming laptop",
        price=999.0,
        quantity=5,
    ),
    Product(
        id=3,
        name="mouse",
        description="gaming mouse",
        price=99.0,
        quantity=10,
    ),
    Product(
        id=4,
        name="keyboard",
        description="gaming keyboard",
        price=99.0,
        quantity=10,
    ),

]


@app.get("/products")  # this REST API endpoint returns a list of products
def get_all_products():
    return products
