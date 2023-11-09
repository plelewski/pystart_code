names = {}

while (answer := input('Podaj imię: ')) != 'koniec':
    counter = names.get(answer,0)
    names[answer] = counter + 1

for n,c in names.items():
    print(n, ' ', c)

print(sorted(names.keys()))
