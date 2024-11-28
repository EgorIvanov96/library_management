# import json
# from typing import List, Union

# from library.books import Book
from library.librarys import Library


def main():
    """Основная функция запуска консольного приложения."""

    library = Library()

    while True:
        print('\nУправление библиотекой')
        print('1. Добавить книгу')
        print('2. Удалить книгу')
        print('3. Поиск книги')
        print('4. Показать все книги')
        print('5. Изменить статус книги')
        print('6. Выйте')

        choice = input('Выберите действие и укажите цифру: ')
        if choice == '1':
            title = input('Введите название: ')
            author = input('Введите автора: ')
            year = input('Введите год издания: ')
            if not year.isdigit():
                print('Ошибка: Укажите год издания числом.')
                continue
            library.add_book(title, author, int(year))
        elif choice == '2':
            book_id = input('Введите ID книги для удаления: ')
            if not book_id.isdigit():
                print('Ошибка: Укажите ID книги числом.')
                continue
            library.delete_book(int(book_id))
        elif choice == '3':
            field = input('Поиск по названию, автору, году издания: ')
            query = input('Введите запрос: ')
            library.search_books(query, field)
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            book_id = input('Введите ID книги чтобы изменить ее статус: ')
            new_status = input("Введите новый статус 'в наличии' или 'выдана'): ")
            if not book_id.isdigit():
                print('Ошибка: Введите ID книги числом.')
                continue
            library.change_status(int(book_id), new_status)
        elif choice == '6':
            print('Выход из программы. Досвидания!')
            break
        else:
            print('Ошибка: Не прравильный выбор. Выберите цырфу из предложанных.')


if __name__ == "__main__":
    main()
