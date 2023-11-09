# def give_vowels(word):
#     vowels = 'aąeęiou'
#     for letter in word:
#         if letter in vowels:
#             group_of_vowels.add(letter)
#     return group_of_vowels
#
# group_of_vowels = set()
# answer = input('Podaj słowo a zwrócę samogłoski: ')
# print(give_vowels(answer))

def get_vowels(word):
    vowels_in_word = set()
    vowels = 'aąeęiou'
    for vowel in vowels:
        if vowel in word or vowel.upper() in word:
            vowels_in_word.add(vowel)

    return vowels_in_word

print(get_vowels('taratere'))
