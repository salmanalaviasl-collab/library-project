 from services.library_manager import LibraryManager

def show_menu():
    print("\n===== سیستم مدیریت کتابخانه =====")
    print("1. افزودن کتاب")
    print("2. حذف کتاب")
    print("3. جستجو بر اساس عنوان")
    print("4. جستجو بر اساس نویسنده")
    print("5. امانت دادن کتاب")
    print("6. بازگرداندن کتاب")
    print("7. نمایش همه‌ی کتاب‌ها")
    print("0. خروج و ذخیره")


def main():
    manager = LibraryManager()
    manager.load()

    while True:
        show_menu()
        choice = input("گزینه‌ی مورد نظر را وارد کنید: ")

        if choice == "1":
            title = input("عنوان کتاب: ")
            author = input("نویسنده: ")
            isbn = input("شابک (ISBN): ")
            manager.add_book(title, author, isbn)
            print("کتاب اضافه شد ✅")

        elif choice == "2":
            isbn = input("شابک کتابی که می‌خواهید حذف کنید: ")
            try:
                manager.remove_book(isbn)
                print("کتاب حذف شد ✅")
            except ValueError as e:
                print(f"خطا: {e}")

        elif choice == "3":
            title = input("عنوان مورد جستجو: ")
            results = manager.find_by_title(title)
            print(results if results else "کتابی پیدا نشد")

        elif choice == "4":
            author = input("نویسنده‌ی مورد جستجو: ")
            results = manager.find_by_author(author)
            print(results if results else "کتابی پیدا نشد")

        elif choice == "5":
            isbn = input("شابک کتابی که می‌خواهید امانت بدهید: ")
            books = [b for b in manager.books if b.isbn == isbn]
            if books:
                try:
                    books[0].borrow()
                    print("کتاب امانت داده شد ✅")
                except ValueError as e:
                    print(f"خطا: {e}")
            else:
                print("کتابی با این شابک پیدا نشد")

        elif choice == "6":
            isbn = input("شابک کتابی که می‌خواهید برگردانید: ")
            books = [b for b in manager.books if b.isbn == isbn]
            if books:
                try:
                    books[0].return_book()
                    print("کتاب برگردانده شد ✅")
                except ValueError as e:
                    print(f"خطا: {e}")
            else:
                print("کتابی با این شابک پیدا نشد")

        elif choice == "7":
            for book in manager.books:
                print(book)

        elif choice == "0":
            manager.save()
            print("ذخیره شد. خداحافظ 👋")
            break

        else:
            print("گزینه‌ی نامعتبر، دوباره امتحان کنید")


if __name__ == "__main__":
    main()
