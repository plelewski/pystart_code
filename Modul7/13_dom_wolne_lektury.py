import json
from requests import get, exceptions

def get_authors_slug(author_name: str) -> str:
    v_auth_response = get('https://wolnelektury.pl/api/authors')
    for author in v_auth_response.json():
        if author_name == author['name']:
            return author['slug']


v_author = input('Podaj imię i nazwisko autora: ')
authors_slug = get_authors_slug(v_author)
book_titles = []

if authors_slug is not None:
    response = get(f'https://wolnelektury.pl/api/authors/{authors_slug}/books/')
    for book in response.json():
        # print(book['title'])
        # print(book.get('title')
        book_titles.append(book['title'])

if len(book_titles) > 0:
    with open('data.json', 'w', encoding='utf8') as file:
        json.dump(book_titles, file, ensure_ascii=False)
