from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import Author,Book
from database import SessionLocal

# Create authors
author1 = Author(name="Harper Lee")
author2 = Author(name="George Orwell")
author3 = Author(name="F. Scott Fitzgerald")
author4 = Author(name="Jane Austen")
author5 = Author(name="J.D. Salinger")
author6 = Author(name="J.K. Rowling")
author7 = Author(name="J.R.R. Tolkien")
author8 = Author(name="C.S. Lewis")
author9 = Author(name="Dan Brown")
author10 = Author(name="Virginia Woolf")
author11 = Author(name="Herman Melville")
author12 = Author(name="Mark Twain")
author13 = Author(name="Aldous Huxley")
author14 = Author(name="Homer")
author15 = Author(name="Charlotte Brontë")
author16 = Author(name="Khaled Hosseini")
author17 = Author(name="Margaret Mitchell")
author18 = Author(name="Oscar Wilde")
author19 = Author(name="Paulo Coelho")
author20 = Author(name="J.R.R. Tolkien")  # Same author as book 7

# Create books
book1 = Book(name="To Kill a Mockingbird", author=author1, number_of_pages=281, author_name=author1.name)
book2 = Book(name="1984", author=author2,number_of_pages=328, author_name=author2.name)
book3 = Book(name="The Great Gatsby", author=author3,number_of_pages=180, author_name=author3.name)
book4 = Book(name="Pride and Prejudice", author=author4,number_of_pages=279, author_name=author4.name)
book5 = Book(name="The Catcher in the Rye", author=author5,number_of_pages=234, author_name=author5.name)
book6 = Book(name="Harry Potter and the Sorcerer's Stone",author=author6, number_of_pages=320, author_name=author6.name)
book7 = Book(name="The Lord of the Rings",author=author7, number_of_pages=1178,author_name=author7.name)
book8 = Book(name="The Hobbit", author=author7, number_of_pages=310,author_name=author8.name)
book9 = Book(name="The Chronicles of Narnia",author=author8, number_of_pages=767,author_name=author9.name)
book10 = Book(name="The Da Vinci Code", author=author9, number_of_pages=454,author_name=author10.name)
book11 = Book(name="To the Lighthouse", author=author10, number_of_pages=209,author_name=author11.name)
book12 = Book(name="Moby-Dick", author=author11, number_of_pages=585,author_name=author12.name)
book13 = Book(name="The Adventures of Huckleberry Finn",author=author12, number_of_pages=366,author_name=author13.name)
book14 = Book(name="Brave New World", author=author13, number_of_pages=325,author_name=author14.name)
book15 = Book(name="The Odyssey", author=author14, number_of_pages=442,author_name=author15.name)
book16 = Book(name="Jane Eyre", author=author15, number_of_pages=594,author_name=author16.name)
book17 = Book(name="The Kite Runner", author=author16, number_of_pages=371,author_name=author17.name)
book18 = Book(name="Gone with the Wind", author=author17, number_of_pages=1037,author_name=author18.name)
book19 = Book(name="The Picture of Dorian Gray",author=author18, number_of_pages=254,author_name=author19.name)


# def data_factory(db: Session = Depends(get_db)):
def data_factory():
    db = SessionLocal() 
    
    print("i got here")
    
    db.add_all([
        author1,
        author2,
        author3,
        author4,
        author5,
        author6,
        author7,
        author8,
        author9,
        author10,
        author11,
        author12,
        author13,
        author14,
        author15,
        author16,
        author17,
        author18,
        author19,
        author20
    ])
    db.add_all([
               book1,
               book2,
               book3,
               book4,
               book5,
               book6,
               book7,
               book8,
               book9,
               book10,
               book11,
               book12,
               book13,
               book14,
               book15,
               book16,
               book17,
               book18,
               book19])
    db.commit()
    
