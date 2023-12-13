#!/usr/bin/env python3

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    price: float
    in_stock: bool

@app.get("/")
def read_root():
    return {"greeting": "welcome to the FastAPI bookstore!"}

@app.get("/books/{book_id}")
def read_item(book_id: int, q: Union[str, None] = None):
    return {"book_id": book_id, "q": q}

@app.put("/books/{book_id}")
def update_item(book_id: int, book: Book):
    return {"book_id": book_id, "title": book.title}
