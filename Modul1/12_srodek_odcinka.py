from math import sqrt

Ax = int(input('Podaj wartość x dla punktu A: '))
Ay = int(input('Podaj wartość y dla punktu A: '))
Bx = int(input('Podaj wartość x dla punktu B: '))
By = int(input('Podaj wartość y dla punktu B: '))

length = sqrt((Ax - Bx) ** 2 + (Ay - By) ** 2)
print('Długość odcinka: ' + str(length))

middle_x = (Ax + Bx) / 2
middle_y = (Ay + By) / 2
print(f'Środek odcinka jest w punktach {middle_x},{middle_y}')
