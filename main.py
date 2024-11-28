import itertools
import os

STATUS = ('в наличии', 'выдана')


class Book:
    new_id = itertools.count().__next__

    def __init__(self, title, author, year):
        self.id = Book.new_id()
        self.title = title
        self.author = author
        self.year = year
        self.status = STATUS[0]


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        if title == '' or author == '' or year == '':
            print('Заполните все поля!')
            return
        book = Book(title, author, year)
        self.books.append(book)
        print('Книга успешно добавлена')

    def remove_book(self, id):
        for book in self.books:
            if book.id == int(id):
                self.books.remove(book)
                print('Книга успешно удаленна.')
                return
        print('Книги с таким ID не найдено!')

    def find_book(self, title=None, author=None, year=None):
        found_books = []
        for book in self.books:
            if book.title == title or book.author == author or book.year == year:
                found_books.append(book)
        return found_books

    def display_books(self):
        for book in self.books:
            print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, "
                  f"Год издания: {book.year}, Статус: {book.status}")

    def update_status(self,  id, status):
        if status not in STATUS:
            print('Неверный статус!')
            return
        for book in self.books:
            if book.id == int(id):
                book.status = status
                print('Статус книги изменен.')
                return
        print('Книги с таким ID не найдено!')


def main():
    """Основная функция проекта."""
    lib = Library()
    lib.add_book('Pomidor', 'kirill', 2009)
    lib.add_book('Pomidor2', 'kirill', 2010)
    lib.add_book('Pomidor3', 'Oleg', 2010)

    while True:
        input('\nНажмите Enter, чтобы продолжить')
        os.system('cls')
        print('1 - Список всех книг.\n'
              '2 - Добавить книгу.\n'
              '3 - Удалить книгу.\n'
              '4 - Найти книгу.\n'
              '5 - Изменить статус книге.\n'
              '0 - Закрыть программу.\n'
              '__________________________')

        command = input('Введите номер команды: ')

        match command:
            case '0':
                exit()
            case '1':
                os.system('cls')
                lib.display_books()
            case '2':
                os.system('cls')
                title = input('Введите название книги: ')
                author = input('Введите автора книги: ')
                year = input('Введите год книги: ')
                lib.add_book(title, author, year)

            case '3':
                os.system('cls')
                id = input('Введите ID книги: ')
                lib.remove_book(id)
            case '4':
                os.system('cls')
                print('Найти')
            case '5':
                os.system('cls')
                id = input('Введите ID книги: ')
                status = input("Введите новый статус на выбор ('в наличии', 'выдана'): ")
                lib.update_status(id, status)


if __name__ == '__main__':
    main()
