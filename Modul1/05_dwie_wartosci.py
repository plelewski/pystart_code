value1 = float(input('Podaj pierwszą liczbę: '))
value2 = float(input('Podaj drugą liczbę: '))

if value1 < value2:
    print('Pierwsza jest większa od drugiej')
elif value1 > value2:
    print('Druga jest większa od pierwszej')
else:
    print('Obie liczby są takie same')
