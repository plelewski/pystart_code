cities = {}
avg_temp = 0

while (answer := input('Podaj nazwę miasta lub koniec: ')) != 'koniec':
    cities[answer] = int(input('Podaj temperaturę dla tego miasta: '))

avg_temp = sum(cities.values())/len(cities.values())
print(f'Średnia temperatura {avg_temp}')
