# man or woman
name = str(input('Podaj swoje imię: '))

# if name[-1].lower() == 'a':
if name.endswith('a'):
    print('Witam Panią')
else:
    print('Witam Pana')

# strong password
password = str(input('Podaj hasło a wygeneruję Ci mocniejsze: '))

print('Twoje nowe hasło', password.lower().replace('a','@').replace('s','$'))

# count word "pies"
sentence = 'pies to najlepszy przyjaciel, ale nie każdy pies to wie'

print(sentence.count('pies'))

# sum numeric values
fruit_sentence = '12 kg jabłek, 10 kg gruszek, 20 kg śliwek'
how_many_kilos = 0

for i in fruit_sentence.split(' '):
    if i.isnumeric():
        how_many_kilos += int(i)

print(f'W sumie jest {how_many_kilos}kg owoców w siatce')
