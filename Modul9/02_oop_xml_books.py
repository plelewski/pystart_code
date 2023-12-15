from datetime import date


class Author:
    def __init__(self, first_name: str, last_name: str, birthday: date):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday

class Book:
    def __init__(self, title: str, kind: str, description: str, summary: str, grade: float):
        self.title = title
        self.kind = kind
        self.description = description
        self.summary = summary
        self.grade = grade
        self.authors = []

    def add_author(self, author: Author):
        self.authors.append(author)


if __name__ == '__main__':
    author1 = Author(first_name='Denis', last_name='Rodman', birthday=date(1961, 5, 13))
    author2 = Author('Tim', 'Keown', date(1960, 1, 1))

    book = Book('Zły do szpiku kości', 'biografia', 'D.Rodman', 'Życie Denisa Rodmana', 4.9)
    book.add_author(author1)
    book.add_author(author2)

    print(book.title)
    print(book.authors[0].first_name)

