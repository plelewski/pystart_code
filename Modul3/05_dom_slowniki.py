# 1
fruits = {'banan':      6.78,
          'jabłko':     4.32,
          'gruszki':    5.43
          }

for name, price in fruits.items():
    if name in ('banan', 'jabłko'):
        print(f'{name} w cenie {price}')

# 1.1
for fruit in fruits:
    if fruit in ('jabłko', 'banan'):
        print(fruits[fruit])

# 2
films = [
        {'title': 'Tytuł 1', 'year': 1994, 'director': 'Spielberg'},
        {'title': 'Tytuł 11', 'year': 1995, 'director': 'Allen'},
        {'title': 'Tytuł 111', 'year': 1996, 'director': 'Allen'},
        {'title': 'Tytuł 1111', 'year': 1997, 'director': 'Spielberg'}
]

for film in films:
    if film.get('director') == 'Spielberg':
        films.remove(film)

print(films)

# 3
animals = {'pies': 4, 'kot': 4, 'kaczka': 2, 'pająk': 8}

max_num_of_legs = 0

for animal in animals:
    if animals[animal] > max_num_of_legs:
        max_num_of_legs = animals[animal]

for animal in animals:
    if animals[animal] == max_num_of_legs:
        print(animal, animals[animal])

# 4
print('###### 4 #####')
animals2 = [
    {'name': 'kot', 'breed': 'syberyjski'},
    {'name': 'pies', 'breed': 'owczarek'},
    {'name': 'jeż', 'breed': 'jeż europejski'}
]

max_lenght = None

for animal in animals2:
    lenght = len(animal['name']) + len(animal['breed'])
    if max_lenght is None or lenght > max_lenght:
        max_lenght = lenght

for animal in animals2:
    lenght = len(animal['name']) + len(animal['breed'])
    if lenght == max_lenght:
        print(animal['name'], lenght)
