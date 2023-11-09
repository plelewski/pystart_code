parzyste= []
nieparzyste = []

while (answer := int(input('Podaj liczbę: '))) != 0:
    if answer % 2 == 0:
        parzyste.append(answer)
    else:
        nieparzyste.append(answer)

print(sorted(set(parzyste)))
print(sorted(set(nieparzyste)))
