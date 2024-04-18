import argparse

print("test")
# Клас для книги
class BookModel:
    def __init__(self, title: str, author: str, year: int, genre: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

# Клас для бібліотеки книг
class Library:
    def __init__(self):
        self.books = []

    # Метод додавання
    def add_book(self, book: BookModel):
        self.books.append(book)
        print(f"До бібліотеки додано книгу: {book.title}")

    # Метод видалення
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
                print(f"Назва: {book.title}, Автор: {book.author}, Рік: {book.year}, Жанр: {book.genre}")

def main():
    # парсер аргументів командного рядка
    parser = argparse.ArgumentParser(description='Управління бібліотекою книг')
    parser.add_argument('command', choices=['add', 'remove', 'list'], help='Команда для виконання')
    parser.add_argument('--title', help='Назва книги')
    parser.add_argument('--author', help='Автор книги')
    parser.add_argument('--year', type=int, help='Рік видання книги')
    parser.add_argument('--genre', help='Жанр книги')


    args = parser.parse_args()

    library = Library()

    # Обробляємо команди
    if args.command == 'add':
        book = BookModel(args.title, args.author, args.year, args.genre)
        library.add_book(book)
    elif args.command == 'remove':
        library.remove_book(args.title)
    elif args.command == 'list':
        library.list_books()

if __name__ == "__main__":
    main()