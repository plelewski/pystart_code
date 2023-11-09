
answer = input('Podaj imię i nazwisko: ')
name, surname = answer.split(' ')

with open('dane_klientow.txt', encoding='utf8', mode='a') as file:
    file.write(f'{name};{surname}\n')
