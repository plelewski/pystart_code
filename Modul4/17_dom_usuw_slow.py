text = 'to jest tekst do obrobki i wywalenia slow na literę t'


for word in text.split():
    print(word) if not(word.startswith('t')) else print('')

