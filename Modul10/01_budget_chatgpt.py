import sqlite3

class ExpenseTracker:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT,
                amount REAL
            )
        ''')
        self.conn.commit()

    def add_expense(self, category, amount):
        self.cursor.execute('''
            INSERT INTO expenses (category, amount) VALUES (?, ?)
        ''', (category, amount))
        self.conn.commit()

    def view_expenses(self):
        self.cursor.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category')
        rows = self.cursor.fetchall()
        if not rows:
            print("Brak wydatków.")
        else:
            print("Zestawienie wydatków:")
            for row in rows:
                print(f"{row[0]}: {row[1]} PLN")

    def menu(self):
        while True:
            print("\n*** MENU ***")
            print("1. Dodaj wydatek")
            print("2. Zobacz wydatki")
            print("3. Wyjście")
            choice = input("Wybierz opcję: ")

            if choice == '1':
                category = input("Podaj kategorię wydatku: ")
                amount = float(input("Podaj kwotę wydatku: "))
                self.add_expense(category, amount)
                print("Wydatek dodany!")
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                print("Dziękujemy. Do widzenia!")
                break
            else:
                print("Niepoprawny wybór. Wybierz ponownie.")


# Utwórz instancję ExpenseTracker i uruchom program
db_name = 'expenses.db'
tracker = ExpenseTracker(db_name)
tracker.menu()
