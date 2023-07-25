# pobierz ciąg znaków i pokaż w odwrotnej kolejności
sentence = input('Napisz coś, cokolwiek: ')
print('odwrócone zdanie to: ', sentence[::-1])

# bez spacji i znaków interpunkcyjnych
drop = (' ', ',', '.')

for char in sentence:
    if char not in drop:
        print(char, end='')
print()

# wyrazy małymi i wielkimi literami naprzemiennie
# 1
sentence = 'Litwo ojczyzno moja Ty jesteś jak zdrowie'

for num,word in enumerate(sentence.split(' ')):
    if num % 2 == 0:
        print(word.upper(), end=' ')
    else:
        print(word.lower(), end=' ')
print()

# 2
new_sentence = ''
new_word = ''

for num,word in enumerate(sentence.split(' ')):
    new_word = word.lower()
    if num % 2 == 0:
        new_word = word.upper()

# najpierw jest spacja, ponieważ do pustego sentence dodajemy spację i pierwszee słowo
    new_sentence = f'{new_sentence} {new_word}'

print(new_sentence)

# wypisać takie, które zaczynają się i kończą na tą samą literę
for word in sentence.split(' '):
    if word[:1] == word[-1:]:
        print(word)
