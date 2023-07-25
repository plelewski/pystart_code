import datetime

curr_year = datetime.date.today().year

birth_year = int(input('Podaj w którym roku się urodziłeś: '))

print(f'Masz teraz rocznikowo {curr_year - birth_year}')

if (birth_year % 4 == 0 and birth_year % 100 !=0) or birth_year % 400 == 0:
    print('To był rok przestępny')
else:
    print('To nie był rok przestępny')
