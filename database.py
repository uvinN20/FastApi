from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

db_url="mysql+pymysql://root:Uvin@#2001@localhost:3306/fastapi_db"
db_url = db_url.replace("@#", "%40%23", 1)
engine = create_engine(db_url, pool_pre_ping=True)


sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
