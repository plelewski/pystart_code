#1
loe = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

answer = int(input('Z którego miejsca z listy podać wartość?: '))

try:
    print(loe[answer])
except IndexError:
    print('Lista ma tylko 10 elementów')

#2
doo = {'jeden': 1,
       'dwa': 2,
       'trzy': 3}

try:
    print(doo['cztery'])
except KeyError as error_message:
    print(error_message)
    print('Nie ma takiego klucza')
finally:
    print('A to koniec')
