
with open('dane_klientow.txt', encoding='utf8', mode='r') as file:
    lines = [line.strip() for line in file.readlines()]


answer = input('Podaj imię i nazwisko: ')
name, surname = answer.split(' ')

v_write = True

for v_rec in lines:
    v_name, v_surname = v_rec.split(';')
    if v_name == name and v_surname == surname:
        v_write = True
        exit()

if v_write:
    with open('dane_klientow.txt', encoding='utf8', mode='a') as file:
        file.write(f'{name};{surname}\n')
else:
    print('duplikat')
