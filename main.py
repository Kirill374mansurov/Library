import itertools
import os

from typing import List


STATUS: List[str] = ['в наличии', 'выдана']


class Book:
    """Класс книги."""
    new_id = itertools.count().__next__

    def __init__(self, title, author, year):
        self.id = Book.new_id()
        self.title = title
        self.author = author
        self.year = year
        self.status = STATUS[0]


class Library:
    """Класс библиотеки, хранящий объекты класса Book."""
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        """Функция добавление книги."""
        if title == '' or author == '' or year == '':
            print('Заполните все поля!')
            return

        book = Book(title, author, year)
        self.books.append(book)
        print('Книга успешно добавлена')

    def remove_book(self, id):
        """Функция удаления книги."""
        for book in self.books:
            if book.id == int(id):
                self.books.remove(book)
                print('Книга успешно удаленна.')
                return

        print('Книги с таким ID не найдено!')

    def find_title_book(self, title):
        """Функция поиска книги по названию."""
        found_books = []

        for book in self.books:
            if book.title == title:
                found_books.append(book)
        return found_books

    def find_author_book(self, author):
        """Функция поиска книги по автору."""
        found_books = []

        for book in self.books:
            if book.author == author:
                found_books.append(book)
        return found_books

    def find_year_book(self, year):
        """Функция поиска книги по году."""
        found_books = []

        for book in self.books:
            if book.year == year:
                found_books.append(book)
        return found_books

    def display_books(self):
        """Функция вывода списка всех книг."""
        for book in self.books:
            print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, "
                  f"Год издания: {book.year}, Статус: {book.status}")

    def update_status(self,  id, status):
        """Функция обновление статуса книги."""
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
                title: str = input('Введите название книги: ')
                author: str = input('Введите автора книги: ')
                year: str = input('Введите год книги: ')
                lib.add_book(title, author, year)

            case '3':
                os.system('cls')
                id: str = input('Введите ID книги: ')

                if id != '':
                    lib.remove_book(id)
                else:
                    print('Введите корректный ID!')

            case '4':
                os.system('cls')
                books = False
                num: str = input(' 1 - Название, 2 - Автор, 3 - Год\nВыберите критерий поиска: ')

                match num:

                    case '1':
                        title: str = input('Введите название книги: ')
                        books = lib.find_title_book(title)

                    case '2':
                        author: str = input('Введите автора книги: ')
                        books = lib.find_author_book(author)

                    case '3':
                        year: str = input('Введите год книги: ')
                        books = lib.find_year_book(year)

                    case _:
                        print('Неправильный критерий!')

                os.system('cls')

                if books:
                    print('Под ваши критерии подходят следующие книги: \n')
                    for book in books:
                        print(f'{book.id}, {book.title}, {book.author}, {book.year}, {book.status}\n')

            case '5':
                os.system('cls')
                id: str = input('Введите ID книги: ')
                status: str = input("Введите новый статус на выбор ('в наличии', 'выдана'): ")

                if id != '':
                    lib.update_status(id, status)
                else:
                    print('Введите коректный ID!')

            case _:
                print('Неправильная команда!')


if __name__ == '__main__':
    main()
