items = {'moneta', 'miecz', 'zbroja'}

parameter = False

while True:
    answer = input('Jaki przedmiot dodać/sprawdzić? (quit - przerywa program)')
    if answer == 'quit':
        break
    elif answer in items:
        print('Już go masz')
    items.add(answer)

print(items)
