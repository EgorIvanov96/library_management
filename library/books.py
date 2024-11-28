class Book:
    """Класс представляющий книги"""
    
    def __init__(self, book_id, title, author, year, status = 'в наличии'):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        """Преобразовываем данные книги в словарь."""

        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status,
        }

    @staticmethod
    def from_dict(data: dict):
        """Создаем объект книги."""

        return Book(
            book_id=data['id'],
            title=data['title'],
            author=data['author'],
            year=data['year'],
            status=data['status'],
        )
