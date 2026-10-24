import os
from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

db_url = os.environ.get("DATABASE_URL")
if not db_url:
    raise RuntimeError("Set DATABASE_URL to your MySQL SQLAlchemy connection URL before starting the API.")
engine = create_engine(db_url, pool_pre_ping=True)


sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
