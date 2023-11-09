pesel = '77022402453'
CONTROL = '13791379131'
total = 0

if len(pesel) != 11:
    print('pesel nie jest prawidłowy')
    quit()

for pesel_digit, pesel_control in zip(pesel, CONTROL):
    total += int(pesel_digit) * int(pesel_control)

if total & 10 != 0:
    print(f'pesel nie jest prawidłowy - suma kontrolna = {total}')
    quit()

print('pesel jest ok')
