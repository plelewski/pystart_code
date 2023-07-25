# 1
from random import choice, choices, shuffle

dishes = {
    'soup': ['pomidorowa', 'żurek', 'krupnik'],
    'dinner': ['schabowy', 'kurczak', 'toffu'],
    'dessert': ['lody', 'ciasto', 'czekolada']
}

for s in dishes.values():
    print(choice(s))

# 2
colors = [chr(9824), chr(9827), chr(9829), chr(9830)]
values = list(range(2,11)) + ['J', 'D', 'K', 'A']
cards = []

for c in colors:
    for v in values:
        cards.append(str(v)+str(c))

print(choices(cards, k=2))
shuffle(cards)
print(cards[:2])
# ze zdjęciem kart z talii
print(cards.pop(), cards.pop())
