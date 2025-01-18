from typing import Annotated

from fastapi import Depends
from sqlmodel import create_engine,Session
# from sqlalchemy.orm import declarative_base
# from sqlalchemy.orm import sessionmaker

def get_session():
    with Session(engine) as session:
        yield session

# SQL_ALCHEMY_DB_URL = "sqlite:///C:/Users/duves/Documents/Duvesh/Learning/FastAPI/Blog-Backend/blog/local.db"
sqlite_file_name = "local.db"
sqlite_url = f"sqlite:///./{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url,connect_args=connect_args)

SessionLocal = Annotated[Session, Depends(get_session)]

#SessionLocal = sessionmaker(bind=engine,autoflush=False)

# Base = declarative_base()