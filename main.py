from library import Library

def main():
    lib = Library()

    while True:
        print("\n=== KÜTÜPHANE MENÜ ===")
        print("1. Kitap Ekle (ISBN ile)")
        print("2. Kitap Sil")
        print("3. Kitapları Listele")
        print("4. Kitap Ara")
        print("5. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            isbn = input("ISBN: ")
            book = lib.add_book(isbn)
            if book:
                print(f"✅ Eklendi: {book}")
            else:
                print("❌ Kitap bulunamadı veya hata oluştu.")
        elif choice == "2":
            isbn = input("Silinecek ISBN: ")
            if lib.remove_book(isbn):
                print("✅ Kitap silindi.")
            else:
                print("❌ Kitap bulunamadı.")
        elif choice == "3":
            for b in lib.list_books():
                print(b)
        elif choice == "4":
            isbn = input("Aranacak ISBN: ")
            book = lib.find_book(isbn)
            print(book if book else "❌ Kitap bulunamadı.")
        elif choice == "5":
            print("👋 Çıkış yapılıyor...")
            break
        else:
            print("❌ Geçersiz seçim.")

if __name__ == "__main__":
    main()
