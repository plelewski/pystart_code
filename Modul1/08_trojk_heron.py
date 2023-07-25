Ax = int(input('Podaj wartość x dla punktu A: '))
Ay = int(input('Podaj wartość y dla punktu A: '))
Bx = int(input('Podaj wartość x dla punktu B: '))
By = int(input('Podaj wartość y dla punktu B: '))
Cx = int(input('Podaj wartość x dla punktu C: '))
Cy = int(input('Podaj wartość y dla punktu C: '))

area = abs((Bx - Ax) * (Cy - Ay) - (By - Ay) * (Cx - Ax)) / 2

print(f'Pole trójkąta wynosi: {area}')
