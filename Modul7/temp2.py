import random

tabela = input('Podaj 5 liczb, ktore beda rozdzielone przecinkiem: ').split(',')
x = random.choice(tabela)
tabela2 = set(tabela)

if len(tabela2) == 5:
    if x == min(tabela2):
        print("Wylosowales najmniejsza liczbe")
    elif x == max(tabela2):
        print("Wylosowales najwieksza liczbe")
    else:
        print("Try again")
else:
    print("Nice reading bro")
