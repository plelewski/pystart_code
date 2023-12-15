import sqlite3
import subprocess
from sys import argv


def get_ips(db_connection):
    cursor = db_connection.cursor()
    res = cursor.execute('SELECT ip from ip_to_check')

    return res


def save_status(db_connection, ip: str, is_up: bool):
    cursor = db_connection.cursor()
    cursor.execute('INSERT INTO log(ip, is_up) VALUES(?, ?)', (ip, int(is_up))) #int(is_up) bo 1 True a 0 False


def check_if_is_up(ip: str) -> bool:
    output = subprocess.run(["ping", "-c", "1", ip], capture_output=True)
    if 'cannot resolve' in output.stderr.decode('utf8'):
        return False

    return True


def setup(db_connection):
        sqls = ['''CREATE TABLE ip_to_check(
            ip TEXT
        )''', '''CREATE TABLE log(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        is_up INTEGER
        )''']

        cursor = db_connection.cursor()

        for sql in sqls:
            cursor.execute(sql)
        db_connection.commit()


with sqlite3.connect('ip_to_check.db') as connection:
    if len(argv) == 2 and argv[1] == 'setup':
        setup(connection)

    for ip, in get_ips(connection):
        save_status(connection, ip, check_if_is_up(ip))
