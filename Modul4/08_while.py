import random

v_num = random.randint(1,20)
number_of_tries = 0
answer = 0

while answer != v_num:
    answer = int(input(f'Zgadnij liczbę z przedziału 1-20: '))
    if answer > v_num:
        print('za duża')
    elif answer < v_num:
        print('Za mała')
    number_of_tries += 1

print(f'Brawo. Ilość prób: {number_of_tries}')
