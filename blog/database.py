from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_ALCHEMY_DB_URL = "sqlite:///./local.db"

connect_args = {"check_same_thread": False}
engine = create_engine(SQL_ALCHEMY_DB_URL,connect_args=connect_args)

SessionLocal = sessionmaker(bind=engine,autoflush=False)

Base = declarative_base()