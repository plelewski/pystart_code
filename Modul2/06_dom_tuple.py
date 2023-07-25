values = tuple(range(12, 1024, 6))

# ile ich jest
print(len(values))

# trzy pierwsze liczby
print(values[:3])

# przedostatni element
print(values[-2])

# co szósty licząc od czwartego
print(values[3::6])

# co trzeci licząc od końca
print(values[::-3])

# średnia ostatnich dziesięciu
print(sum(values[-10::]) / 10)

# wyświetlanie elementów
person = ('Jan', 'Kowalski', 40)
print(f'Imię: {person[0]}')
print(f'Nazwisko: {person[1]}')
print(f'Lat: {person[2]}')

# wyświetlanie trudniejsze
calculations = ((1,2,3), (4,5,6), (7,8,9,))

for eg in calculations:
    print(f'{eg[0]} + {eg[1]} + {eg[2]} = {sum(eg)}')

