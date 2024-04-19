# Клас для книги
class BookModel:
    def __init__(self, title: str, author: str, year: int, genre: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

# Клас для журналу
class MagazineModel:
    def __init__(self, title: str, author: str, year: int, volume: int):
        self.title = title
        self.author = author
        self.year = year
        self.volume = volume

# Клас для бібліотеки книг
class Library:
    def __init__(self):
        self.books = []

    # Метод додавання книги
    def add_book(self, book):
        self.books.append(book)
        print(f"До бібліотеки додано книгу: {book.title}")

    # Метод видалення книги
    def remove_book(self, title: str):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"З бібліотеки видалено книгу: {title}")
                return
        print(f"Книга '{title}' відсутня в бібліотеці")

    # Метод для виведення списку книг
    def list_books(self):
        if not self.books:
            print("У бібліотеці немає жодної книги")
        else:
            print("Список книг у бібліотеці:")
            for book in self.books:
                if isinstance(book, BookModel):
                    print(f"Книга: {book.title}, Автор: {book.author}, Рік: {book.year}, Жанр: {book.genre}")
                elif isinstance(book, MagazineModel):
                    print(f"Журнал: {book.title}, Автор: {book.author}, Рік: {book.year}, Том: {book.volume}")

    # Метод для збереження книг у файл
    def save_books_to_file(self, filename):
        with open(filename, 'w') as file:
            for book in self.books:
                if isinstance(book, BookModel):
                    file.write(f"Book,{book.title},{book.author},{book.year},{book.genre}\n")
                elif isinstance(book, MagazineModel):
                    file.write(f"Magazine,{book.title},{book.author},{book.year},{book.volume}\n")

    # Метод для завантаження книг з файлу
    def load_books_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == 'Book':
                    book = BookModel(data[1], data[2], int(data[3]), data[4])
                    self.add_book(book)
                elif data[0] == 'Magazine':
                    magazine = MagazineModel(data[1], data[2], int(data[3]), int(data[4]))
                    self.add_book(magazine)

def main():
    library = Library()

    while True:
        print("\nВиберіть опцію:")
        print("1. Додати книгу")
        print("2. Видалити книгу")
        print("3. Вивести список книг")
        print("4. Зберегти дані у файл")
        print("5. Завантажити дані з файлу")
        print("6. Вихід")

        choice = input("Введіть номер опції: ")

        if choice == '1':
            title = input("Введіть назву книги: ")
            author = input("Введіть автора книги: ")
            year = int(input("Введіть рік видання книги: "))
            genre = input("Введіть жанр книги: ")
            book = BookModel(title, author, year, genre)
            library.add_book(book)
        elif choice == '2':
            title = input("Введіть назву книги, яку бажаєте видалити: ")
            library.remove_book(title)
        elif choice == '3':
            library.list_books()
        elif choice == '4':
            filename = input("Введіть назву файлу для збереження: ")
            library.save_books_to_file(filename)
            print("Дані збережено у файл")
        elif choice == '5':
            filename = input("Введіть назву файлу для завантаження: ")
            library.load_books_from_file(filename)
            print("Дані завантажено з файлу")
        elif choice == '6':
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
