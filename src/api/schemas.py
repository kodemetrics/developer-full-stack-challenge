from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4


class AuthorSchema(BaseModel):
    # id: Optional[UUID] = uuid4()
    name: str
    # number_of_books: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class BookSchema(BaseModel):
    # id: Optional[UUID] = uuid4()
    name: str
    author_name: str
    number_of_pages: int
    author_id:int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class UserSchema(BaseModel):
    # id: Optional[UUID] = uuid4()
    # id: str
    username: str
    password: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
