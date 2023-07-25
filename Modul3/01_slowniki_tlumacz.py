# tłumaczenie ang/pol
dictionary = {'dog': 'pies', 'cat': 'kot', 'boy': 'chłopiec', 'girl': 'dziewczynka'}

which_way = input('Wpisz ang jeśli chcesz tłumaczyć na angielski lub pol jeśli na polski: ')
if which_way.lower() != 'ang' and which_way.lower() != 'pol':
    print('nie ma takie jopcji')
    quit()

what_word = input('Podaj słowo do tłumaczenia: ')
translated_word = None

for english_word, polish_word in dictionary.items():
    if which_way == 'ang' and english_word == what_word:
        translated_word = polish_word
        break
    elif which_way == 'pol' and polish_word == what_word:
        translated_word = english_word
        break

if translated_word is not None:
    print(f'Tłumaczenie to {translated_word}')
else:
    print('Nie ma takiego słowa')
