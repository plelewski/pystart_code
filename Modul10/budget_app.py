import sqlite3
from budget_model import Model
from datetime import datetime


class Application:
    def __init__(self):
        pass

    def menu(self):
        while True:
            print('\n*** MENU ***')
            print('1: Dodaj wydatek')
            print('2: Usuń wydatek/przychód')
            print('3: Zobacz wydatki/przychody')
            print('4: Dodaj przychód')
            print('5: Wyjście')
            choice = input('Wybierz opcję: ')

            if choice == '1':
                name = input('Podaj nazwę dla wydatku: ')
                category = input('Podaj kategorię wydatku: ')
                amount = float(input('Podaj kwotę wydatku: '))
                when = datetime.strptime(input('Podaj datę czynności w formacie yyyy-mm-dd: '), '%Y-%m-%d').date()
                mod.add_item(name, category, amount * -1, when)

            elif choice == '2':
                answer_exp_id = int(input("Podaj id wydatku: "))
                mod.delete_item(answer_exp_id)

            elif choice == '3':
                for item in mod.list_items():
                    print(item)

            elif choice == '4':
                name = input('Podaj nazwę dla przychodu: ')
                category = input('Podaj kategorię przychodu: ')
                amount = float(input('Podaj kwotę przychodu: '))
                when = datetime.strptime(input('Podaj datę czynności w formacie yyyy-mm-dd: '), '%Y-%m-%d').date()
                mod.add_item(name, category, amount, when)

            elif choice == '5':
                print("Dziękujemy. Do widzenia!")
                break
            else:
                print("Niepoprawny wybór. Wybierz ponownie.")

if __name__ == '__main__':
    with sqlite3.connect('my_budget.db') as conn:
        mod = Model(conn)
        mod.init_db()

        app = Application()
        app.menu()
