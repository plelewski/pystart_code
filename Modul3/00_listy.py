sentence = input('Podaj jakieś zdanie: ')
num_of_words = sentence.split(' ')

print(f'Ilość słów w zdaniu: {len(num_of_words)}')
print(f'Ilość znaków w zdaniu: {len(sentence)}')

# najmniejsza i największa liczba
numbers = []

for _ in range(5):
    num = int(input('Podaj liczbę: '))
    numbers.append(num)

print(f'najmniejsza liczba: {min(numbers)}, największa {max(numbers)} oraz średnia arytmetyczna {sum(numbers)/len(numbers)}')

# wyświetl posortowane imiona bez powtórzeń
full_names = 'Adam Mickiewicz, Adam Asnyk, Zbigniew Nienacki'
names = []
internal = []

for name in full_names.split(', '):
    internal = name.split(' ')
    # u Kacpra first_name, last_name = name.split(' ')
    if internal[0] not in names:
        names.append(internal[0])

print(sorted(names, reverse=True))
