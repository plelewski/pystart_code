products = {
    'bułka': 1,
    'chleb': 7,
    'cukier': 5,
    'mąka': 4,
    'mleko': 4
}

cart = {}
paid_value = 0

print(products)

while (answer := input('Co włożyć do koszyka? (podsumuj kończy zakupy: ')) != 'podsumuj':
    counter = cart.get(answer, 0)
    cart[answer] = counter + 1
    # sprytniejsze rozwiązanie
    # cart[answer] = cart.get(answer, 0) + int(input('Ile sztuk: '))

for p,q in cart.items():
    paid_value += products[p] * q
    print(p, ' ', q, ' ', products[p] * q)

print('Do zapłaty: ', paid_value)
