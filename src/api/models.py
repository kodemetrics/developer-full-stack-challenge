from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.sql import func


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String)
    author_name = Column(String)
    number_of_pages = Column(Integer)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String)
    # number_of_books = Column(Integer)
    books = relationship("Book", back_populates="author")


class User(Base):
    __tablename__ = "users"
    # id = Column(String, primary_key=True, index=True)
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    createdAt = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
