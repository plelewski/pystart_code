value = str(input('Podaj liczbę całkowitą: '))

if value == value[::-1]:
    print('To palindorom')
else:
    print('To nie jest palindorm')
