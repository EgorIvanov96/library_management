from typing import List
import json

from .books import Book


class Library:
    """Класс для управления библиотекой."""

    def __init__(self, storage_file = 'library.json'):
        self.storage_file = storage_file
        self.books: List[Book] = []
        self._load_books()

    def _load_books(self):
        """Загрузить книгу из файла."""

        try:
            with open(self.storage_file, 'r') as file:
                data = json.load(file)
                self.books = [Book.from_dict(book) for book in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def _save_books(self):
        """Сохранение книги."""

        with open(self.storage_file, 'w') as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)

    def add_book(self, title: str, author: str, year: int):
        """Добавление новой книги в библиотеку."""

        new_id = max([book.id for book in self.books], default=0) + 1
        new_book = Book(book_id=new_id, title=title, author=author, year=year)
        self.books.append(new_book)
        self._save_books()
        print(f'Книга добавлена: {new_book.to_dict()}')

    def delete_book(self, book_id: int):
        """Удалить книгу по id."""

        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self._save_books()
                print(f'Книга с id {book_id} удалена.')
                return
        print(f'Ошибка: Книга с таким id {book_id} не найдена.')

    def search_books(self, query: str, field: str):
        """Поиск книги по названию, автору, году."""

        fields_mapping = {
        'название': 'title',
        'автор': 'author',
        'год издания': 'year'
        }
        field = field.lower()
        if field not in fields_mapping:
            print('Ошибка: Не верное поле. Используйте название, автора, год издания.')
            return
        
        eng_field = fields_mapping[field]

        results = [
            book
            for book in self.books
            if str(getattr(book, eng_field, '')).lower() == query.lower()
        ]
        if results:
            print('Результат поиска:')
            for book in results:
                print(book.to_dict())
        else:
            print(f'Не найдено книги с {field} соответствующих {query}.')

    def display_books(self):
        """Отображение всех книг."""

        if not self.books:
            print('В библиотеки нет книг.')
        else:
            print("Книги, которые есть в библиотеки:")
            for book in self.books:
                print(book.to_dict())

    def change_status(self, book_id: int, new_status: str):
        """Изменение статуса книгу."""

        for book in self.books:
            if book.id == book_id:
                if new_status in ['в наличии', 'выдана']:
                    book.status = new_status
                    self._save_books()
                    print(f'Статус книги обновлен: {book.to_dict()}')
                    return
                else:
                    print('Ошибка: Неверный статус. Используйте в наличии или выдана.')
                    return
        print(f'Ошибка: Книга с id {book_id} не найдена.')
