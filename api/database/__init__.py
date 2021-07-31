import os
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative.api import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "1230")
DB_DATABASE = os.getenv("DB_DATABASE", "qrgen")
POSTGRES_URL = os.getenv("POSTGRES_URL", "localhost:5432/")
DATABASE_URI = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{POSTGRES_URL}{DB_DATABASE}"

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()