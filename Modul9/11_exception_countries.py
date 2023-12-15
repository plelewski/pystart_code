import json

from requests import get, exceptions
from json import load, dump


def get_capital(country: str):
    url = f'https://restcountries.com/v3.1/name/{country}'
    response = get(url)
    output = response.json()[0]

    return output['capital'][0]


def load_capitals() -> dict:
    try:
        with open('capitals.json') as file:
            return load(file)
    except FileNotFoundError:
        return {}


capitals = load_capitals()
country = input('Podaj nazwę kraju: ')

try:
    if country in capitals:
        print('Mam już w bazie')
        capital = capitals[country]
    else:
        capital = get_capital(country)

    print(capital)
    capitals[country] = capital
    with open('capitals.json', mode='w') as file:
        json.dump(capitals, file)
except KeyError:
    print('Nie mam takiego kraju')
except exceptions.ConnectionError:
    print('Brak netu albo nieprawidłowy adres')
