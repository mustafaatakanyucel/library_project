import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from library import Library

TEST_FILE = "test_library.json"

@pytest.fixture
def lib():
    # Her testten önce temiz bir test dosyası oluştur
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    library = Library(TEST_FILE)
    yield library
    # Testten sonra dosyayı sil
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_add_book_success(lib):
    isbn = "9780140328721"  # OpenLibrary güncel verisi
    book = lib.add_book(isbn)
    assert book is not None
    assert book.title.lower() == "fantastic mr. fox"
    assert "roald" in book.author.lower()
    assert lib.find_book(isbn) is not None

def test_add_book_invalid_isbn(lib):
    # Geçersiz ISBN ekleme
    isbn = "0000000000"
    book = lib.add_book(isbn)
    assert book is None
    # Liste boş kalmalı
    assert len(lib.list_books()) == 0

def test_remove_book_success(lib):
    isbn = "9780140328721"
    lib.add_book(isbn)
    removed = lib.remove_book(isbn)
    assert removed is True
    # Artık listede olmamalı
    assert lib.find_book(isbn) is None

def test_remove_book_not_found(lib):
    isbn = "1234567890"
    removed = lib.remove_book(isbn)
    assert removed is False

def test_list_books(lib):
    isbn1 = "9780140328721"  # Fantastic Mr. Fox
    isbn2 = "9780439064873"  # Harry Potter and the Chamber of Secrets
    lib.add_book(isbn1)
    lib.add_book(isbn2)
    books = lib.list_books()
    assert len(books) == 2
    titles = [b.title.lower() for b in books]
    assert "fantastic mr. fox" in titles
    assert "harry potter and the chamber of secrets" in titles

def test_find_book_not_found(lib):
    book = lib.find_book("9999999999")
    assert book is None
