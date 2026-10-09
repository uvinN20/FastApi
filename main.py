from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlalchemy import inspect
from sqlalchemy.orm import Session

from database import engine, get_db
from database_model import Base, Product as ProductRecord
from models import Product

default_products = [
    Product(id=1, name="phone", description="budget phone", price=99.0, quantity=10),
    Product(id=2, name="laptop", description="gaming laptop", price=999.0, quantity=5),
    Product(id=3, name="mouse", description="gaming mouse", price=99.0, quantity=10),
    Product(id=4, name="keyboard", description="gaming keyboard", price=99.0, quantity=10),
]


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    products_table_exists = inspect(engine).has_table(ProductRecord.__tablename__)
    Base.metadata.create_all(bind=engine)

    if not products_table_exists:
        with Session(engine) as db:
            db.add_all(
                ProductRecord(**product.model_dump()) for product in default_products
            )
            db.commit()

    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def greet():
    return "welcome to the program!"


@app.get("/products", response_model=list[Product])
def get_all_products(db: Session = Depends(get_db)) -> list[Product]:
    products = db.query(ProductRecord).all()
    return [Product.model_validate(product) for product in products]


@app.get("/product/{id}", response_model=Product | dict[str, str])
def get_product_by_id(id: int, db: Session = Depends(get_db)) -> Product | dict[str, str]:
    product = db.get(ProductRecord, id)
    if product is None:
        return {"error": "Product not found"}
    return Product.model_validate(product)


@app.post("/product", response_model=Product)
def add_product(product: Product, db: Session = Depends(get_db)) -> Product:
    product_record = ProductRecord(**product.model_dump())
    db.add(product_record)
    db.commit()
    db.refresh(product_record)
    return Product.model_validate(product_record)


@app.delete("/product/{id}")
def delete_product(id: int, db: Session = Depends(get_db)) -> str:
    product = db.get(ProductRecord, id)
    if product is None:
        return "Product not found"

    db.delete(product)
    db.commit()
    return "Product deleted successfully"


@app.put("/product/{id}")
def update_product(
    id: int, product: Product, db: Session = Depends(get_db)
) -> str:
    product_record = db.get(ProductRecord, id)
    if product_record is None:
        return "Product not found"

    for field, value in product.model_dump().items():
        setattr(product_record, field, value)
    db.commit()
    return "Product updated successfully"

