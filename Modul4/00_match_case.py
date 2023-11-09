answer = int(input('Podaj numer miesiąca: '))

days = {
    1: 'Styczeń',
    2: 'Luty',
    3: 'Marzec'
}

# w python 3.9 nie ma match ;/
# match answer:
#     case 1:
#         print('to jest styczeń')
#     case 2:
#         print('to jest luty')
#     case _:
#         print('to inny miesiąc')
#         quit()

if answer not in days:
    print('Nie mam takiego miesiąca w słowniku')
else:
    print(f'Ten miesiąc to {days[answer]}')
