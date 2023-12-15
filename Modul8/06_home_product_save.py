from datetime import date

products = set()

# while (product_name = input('Podaj nazwę produktu')) != koniec:
while True:
    answer = input('Podaj nazwę produktu: ')
    if answer == 'koniec':
        break
    products.add(answer)

today = date.today()
with open(f'{today.day}{today.month}{today.year}.txt', encoding='utf8', mode='w') as file:
    for product in products:
        file.write(f'{product}\n')
        # file.write('\n'.join(product))
