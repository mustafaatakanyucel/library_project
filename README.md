
# 📚 Library Project
**Python + FastAPI ile OOP tabanlı Kütüphane Uygulaması**

## 🔹 Öne Çıkan Özellikler
- Terminal uygulaması ile kitap ekleme, silme, listeleme ve arama
- FastAPI tabanlı REST API entegrasyonu
- OpenLibrary API ile ISBN’den kitap bilgisi çekme
- Pytest ile tüm fonksiyonların test edilmesi

---

## 🔹 Proje Açıklaması
Bu proje, Python ile OOP temelleri kullanılarak geliştirilmiş bir kütüphane uygulamasıdır.  
- **Aşama 1 & 2:** Terminal tabanlı uygulama ile kitap ekleme, silme, listeleme ve arama yapılabilir.  
- **Aşama 3:** FastAPI kullanılarak API sunucusu oluşturulmuş ve OpenLibrary API ile kitap bilgileri çekilebilmektedir.

---

## 🚀 Kurulum

### 1️⃣ Repo’yu klonlama
```bash
git clone https://github.com/mustafaatakanyucel/library_project.git
cd library_project 
```
### 2️⃣ Bağımlılıkları kurma
```bash
pip install -r requirements.txt
```
### 🖥️ Kullanım (Usage)
Terminal Uygulaması (Aşama 1 & 2)
```bash
python main.py
```
Kitap ekle, sil, ara veya listele seçeneklerini terminal üzerinden kullanabilirsin.
### API Sunucusu (Aşama 3)
```bash
uvicorn api:app --reload
```
Sunucu başlatıldıktan sonra Swagger UI üzerinden test edebilirsin:
http://127.0.0.1:8000/docs

| Method | Endpoint      | Açıklama                             | Body Örneği               |
| ------ | ------------- | ------------------------------------ | ------------------------- |
| GET    | /books        | Kütüphanedeki tüm kitapları listeler | -                         |
| POST   | /books        | ISBN ile kitap ekler                 | {"isbn": "9780140328721"} |
| DELETE | /books/{isbn} | ISBN’e göre kitabı siler             | -                         |

### 🧪 Test Senaryoları

Projede pytest ile testler yazılmıştır:

test_add_book_success: Geçerli ISBN ile kitap ekleme

test_add_book_invalid_isbn: Geçersiz ISBN ile ekleme denemesi

test_remove_book_success: Kitap silme

test_remove_book_not_found: Mevcut olmayan ISBN ile silme

test_list_books: Kitapların listelenmesi

test_find_book_not_found: Aranan ISBN bulunamazsa

Testleri çalıştırmak için:
```bash
pytest tests/
```
### 💡 Bonus: Commit Geçmişi

Aşama 1 tamamlandı → Terminal uygulaması eklendi

Aşama 2 tamamlandı → Kitap ekleme, silme, listeleme, arama fonksiyonları eklendi

Aşama 3 tamamlandı → FastAPI ile API servisi entegre edildi

### 📌 Notlar

Swagger üzerinden API’yi test edebilirsiniz.

Python 3.9+ tavsiye edilir.
