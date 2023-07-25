# 1
countries = [
    {'country': 'Polska', 'capital': 'Warsaw', 'lang': 'polski'},
    {'country': 'Niemcy', 'capital': 'Berlin', 'lang': 'niemiecki'}
]

print()

countries.append(
    {
        'country': input('Podaj kraj: '),
        'capital': input('Podaj stolicę: '),
        'lang': input('Podaj język urzędowy: ')
    }
)

print(countries)

# 2
from random import choice

capitals = {
    'Polska': 'Warszawa',
    'Ukraina': 'Kijów',
    'Czechy': "Praga"
}

# nie można zrobić random na liście, nawet na kluczu
# dlatego też należy kluczę przerobić na listę i wtedy taki choice jest możliwy
selected_country = choice(list(capitals.keys()))
print(selected_country)
