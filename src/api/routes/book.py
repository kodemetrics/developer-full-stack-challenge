from fastapi import APIRouter, Depends, HTTPException, status
from typing import Union, List
from sqlalchemy.orm import Session
from database import get_db
from models import Book
from models import Author
from schemas import BookSchema


api_router = APIRouter()


@api_router.get("/api/v1/books/")
def fetch_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    # books = db.query(Book).join(Author).all()

    # Execute the raw query
    result = db.execute(
        "SELECT * FROM books as b join authors as a on a.id = b.author_id")
    # books = result.fetchall()
    return books


@api_router.post("/api/v1/books/")
def create_book(book: BookSchema,db: Session = Depends(get_db)):
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return {"status": "success", "data": new_book}

@api_router.put("/api/v1/books/{id}")
def update_book(id: int, book: BookSchema,db: Session = Depends(get_db)):
    books = db.query(Book).get(id)
    if books:
        books.name = book.name
        books.number_of_pages = book.number_of_pages
        books.author_name = book.author_name
        db.commit()
        db.refresh(books)
    else:
        raise HTTPException(
            status_code=404, detail=f" author with id {id} not found")

    return {"status": "success", "data": books, "message": f" author with id {id} updated sucessfully"}


@api_router.delete("/api/v1/books/{id}")
def delete_book(id: int, db: Session = Depends(get_db)):
    books = db.query(Book).get(id)
    if books:
        db.delete(books)
        db.commit()
        db.close()
    else:
        raise HTTPException(
            status_code=404, detail=f" book with id {id} not found")
    return {"status": "success", "data": books, "message": f" author with id {id} deleted sucessfully"}
