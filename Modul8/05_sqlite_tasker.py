import sqlite3
from sys import argv


def setup():
    with sqlite3.connect('tasker2.db') as connection:
        sql = '''CREATE TABLE tasks(
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name VARCHAR(100) UNIQUE NOT NULL,
            is_done TINYINT(1) DEFAULT 0
        )'''

        cur = connection.cursor()
        cur.execute(sql)
        connection.commit()


def add_task():
    answer_task_name = input('Podaj nazwę zadania: ')

    with sqlite3.connect('tasker2.db') as connection:
        cur = connection.cursor()
        cur.execute('INSERT INTO tasks(task_name) VALUES (?)', (answer_task_name, ))
        connection.commit()


def complete_task():
    answer_task_id = input('Podaj id zadania, które zrobiłeś: ')

    with sqlite3.connect('tasker2.db') as connection:
        cur = connection.cursor()
        cur.execute('UPDATE tasks SET is_done = 1 WHERE task_id = (?)', answer_task_id)
        connection.commit()


def show_tasks():
    with sqlite3.connect('tasker2.db') as connection:
        cur = connection.cursor()
        cur.execute('SELECT task_id from tasks')
        row_count = len(cur.fetchall())
        if row_count > 0:
            print('Lista zadań:')
            print('-' * 15)
            for task in cur.execute('''
            SELECT task_id, task_name, 
                case is_done when 0 then 'do wykonania' 
                             else 'wykonane'
                end as Is_done
            FROM tasks
            ORDER by is_done, task_name'''):
                print(task)
            print('-' * 15)


def main():
    while True:
        show_tasks()
        print('''
        Co chcesz zrobić?:
        0 - dodaj nowe zadanie
        1 - ustaw zadanie jako zrealizowane
        e - wyjście z programu
        ''')
        answer = input('Twój wybór: ')

        if answer == '0':
            add_task()
        elif answer == '1':
            complete_task()
        elif answer == 'e':
            exit()
        else:
            print('Zweryfikuj swój wybór')


if __name__ == "__main__":
    if len(argv) == 2 and argv[1] == 'setup':
        setup()

    main()
