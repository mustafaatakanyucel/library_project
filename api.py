from fastapi import FastAPI
from pydantic import BaseModel
from library import Library

app = FastAPI(title="Library API", version="1.0")
lib = Library()

class ISBNRequest(BaseModel):
    isbn: str

class BookResponse(BaseModel):
    title: str
    author: str
    isbn: str

@app.get("/books", response_model=list[BookResponse])
def get_books():
    return [b.__dict__ for b in lib.list_books()]

@app.post("/books", response_model=BookResponse)
def add_book(req: ISBNRequest):
    book = lib.add_book(req.isbn)
    if book:
        return book.__dict__
    return {"title": "Not Found", "author": "N/A", "isbn": req.isbn}

@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    if lib.remove_book(isbn):
        return {"message": "Kitap silindi"}
    return {"message": "Kitap bulunamadı"}
