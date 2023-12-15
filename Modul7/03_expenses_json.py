from json import dump, load

expenses = []

while True:
    answer = input('[d] Dodaj wydatek [w] Wypisz wszystkie [e] wyjście: ')
    if answer == 'e':
        break
    elif answer == 'd':
        answer_desc = input('Czego dotyczy wydatek? ')
        answer_value = int(input('Podaj kwotę w pełnych złotych '))

        with open('wydatki.json', 'w') as file:
            expenses.append({
                "desc": answer_desc,
                "value": answer_value
            })
            dump(expenses, file)
    else:
        with open('wydatki.json', 'r') as file:
            expenses = load(file)
            for expense in expenses:
                print(expense.get('desc'), expense.get('value'))
