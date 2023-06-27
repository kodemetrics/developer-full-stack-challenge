from fastapi import APIRouter, Depends, HTTPException, status
from typing import Union, List
from sqlalchemy.orm import Session
from database import get_db
from models import Author
from schemas import AuthorSchema


api_router = APIRouter()


@api_router.get("/api/v1/authors/")
def fetch_authors(db: Session = Depends(get_db)):
    # authors = db.query(Author).all()
    # Execute the raw query
    raw_query = """
    SELECT authors.id,authors.name, COUNT(books.id) AS number_of_books
    FROM authors
    LEFT JOIN books ON authors.id = books.author_id
    GROUP BY authors.id, authors.name
    """
    result = db.execute(raw_query)
    authors = result.fetchall()
    return authors


@api_router.post("/api/v1/authors/")
def create_author(author: AuthorSchema,db: Session = Depends(get_db)):
    new_author = Author(**author.dict())
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return {"status": "success", "data": new_author}


@api_router.put("/api/v1/authors/{id}")
def update_author(id: int, author: AuthorSchema, db: Session = Depends(get_db)):

    authors = db.query(Author).get(id)
    if authors:
        authors.name = author.name
        # authors.number_of_books = author.number_of_books
        db.commit()
        db.refresh(authors)
    else:
        raise HTTPException(
            status_code=404, detail=f" author with id {id} not found")

    return {"status": "success", "data": authors, "message": f" author with id {id} updated sucessfully"}


@api_router.delete("/api/v1/authors/{id}")
def delete_author(id: int, author: AuthorSchema, db: Session = Depends(get_db)):
    authors = db.query(Author).get(id)
    if authors:
        db.delete(authors);
        db.commit()
        db.close()
    else:
        raise HTTPException(
            status_code=404, detail=f" author with id {id} not found")
    return {"status": "success", "data": authors, "message": f" author with id {id} deleted sucessfully"}

