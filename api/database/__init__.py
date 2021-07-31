import os
from decouple import config
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative.api import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker

DATABASE_USER = config("DATABASE_USER", None)
DATABASE_PASSWORD = config("DATABASE_PASSWORD", None)
DATABASE_NAME = config("DATABASE_NAME", None)
DATABASE_SERVER = config("DATABASE_SERVER", None)
DATABASE_PORT = config("DATABASE_PORT", 5432)
DATABASE_URI = f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_SERVER}:{DATABASE_PORT}/{DATABASE_NAME}"

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