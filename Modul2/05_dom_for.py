# parzyste od 2 do liczby, suma i średnia
value = int(input('Podaj jakąś liczbę '))
total = 0
counter = 0

for i in range(2, value+1, 2):
    print(i, end=',')
    counter += 1
    total += i
print()
print(f'suma liczb {total} a średnia to {total/counter}')

# potęga 2,3,4,5 bez użycia **
value = int(input('Podaj liczbę: '))
result = value

for i in range(2,6):
    result *= value
    print(f'Liczba {value} do potęgi {i} wynosi {result}')

# znaki i ich ascii
sentence = 'Cały czas samopoczucie złe'

for letter in sentence:
    print(letter, ord(letter), end=' ')
print()

# czy liczba pierwsza
number = int(input('Podaj liczbę a sprawdzę czy jest to liczba pierwsza: '))
half = number // 2

counter = 0

for i in range(2, half+1):
    if number % i == 0:
        counter += 1

if counter > 0:
    print('To nie jest liczba pierwsza')
else:
    print('Tak to jest liczba pierwsza')

# czy liczba pierwsza wersja 2
from math import sqrt, ceil
is_prime = True

for div in range(2, ceil(sqrt(number))+1):
    if number % div == 0:
        is_prime = False
        break

if is_prime:
    print('Liczba jest pierwsza')
else:
    print('To nie jest liczba pierwsza')
