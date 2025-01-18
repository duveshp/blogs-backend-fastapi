# from sqlalchemy import Integer,Column,String
# from .database import Base
from typing import Optional

from sqlmodel import Field, SQLModel, Session
from .database import engine

# class Blog(Base):
#     __tablename__="blogs"
#     id = Column(Integer,primary_key=True,index=True)
#     title = Column(String)
#     body = Column(String)

class Blog2(SQLModel, table=True):
    id :int =  Field(primary_key=True)
    title :str
    body :str
    published_at:Optional[bool] = False

class FileRecord(SQLModel, table=True):
    id :int =  Field(primary_key=True)
    filename :str
    filepath :str