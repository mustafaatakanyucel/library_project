import json
import httpx
from book import Book


class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.books = [Book(**b) for b in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def save_books(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([b.__dict__ for b in self.books], f, indent=4)

    def list_books(self):
        return self.books

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def remove_book(self, isbn):
        book = self.find_book(isbn)
        if book:
            self.books.remove(book)
            self.save_books()
            return True
        return False

    def add_book(self, isbn):
        url = f"https://openlibrary.org/isbn/{isbn}.json"

        try:
            # Yönlendirmeleri takip ederek isteği gönder
            response = httpx.get(url, timeout=10, follow_redirects=True)
            response.raise_for_status()  # HTTP hatalarını kontrol et

            data = response.json()

            # Kitap başlığını al
            title = data.get("title", "Unknown Title")

            # Yazar adını almak için:
            # 'authors' anahtarının varlığını ve bir liste olduğunu kontrol et
            author_name = "Unknown Author"
            authors_data = data.get("authors")

            if authors_data and isinstance(authors_data, list):
                first_author_info = authors_data[0]

                if isinstance(first_author_info, dict):
                    # Eğer 'name' yoksa, yazar key üzerinden çağrı yap
                    author_name = first_author_info.get("name")
                    if not author_name and "key" in first_author_info:
                        try:
                            author_url = f"https://openlibrary.org{first_author_info['key']}.json"
                            author_resp = httpx.get(author_url, timeout=10)
                            author_resp.raise_for_status()
                            author_name = author_resp.json().get("name", "Unknown Author")
                        except Exception:
                            author_name = "Unknown Author"

            # Kitap nesnesini oluştur ve kaydet
            book = Book(title=title, author=author_name, isbn=isbn)
            self.books.append(book)
            self.save_books()

            print(f"Kitap başarıyla eklendi: {book}")
            return book

        except httpx.HTTPStatusError as e:
            # Kitap bulunamazsa (404) veya başka bir HTTP hatası olursa
            print(f"Hata: Kitap bulunamadı veya API hatası oluştu. Durum Kodu: {e.response.status_code}")
            return None
        except (httpx.RequestError, json.JSONDecodeError) as e:
            # Bağlantı veya JSON çözümleme hatası
            print(f"Hata: API isteği veya JSON verisi okunurken bir sorun oluştu: {e}")
            return None