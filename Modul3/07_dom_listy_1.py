# 2
import random
from random import randint, shuffle, choice

words = ['laptop', 'pajacyk', 'rzeka', 'robak', 'parapet']

# print('Losuję słowo')
# word_num = randint(0, len(words)-1)
# word = words[word_num]
# shuffled_word = list(word)
# shuffle(shuffled_word)
# shuffled_word = ''.join(shuffled_word)
#
# print(f'Co to za słowo? {shuffled_word}')
#
# for i in range(0,3):
#     answer = input('? ')
#     if answer == word:
#         print(f'Gratulacje. Zgadłeś za {i} razem')
#         break
#     if i == 2:
#         print('To koniec')

# 2.1
letters = list(choice(words))
shuffle(letters)

print('Słowo do odgadnięcia to', ''.join(letters))

# reszta podobnie