from datetime import datetime, timedelta


start_date = datetime.strptime(input('Podaj datę rozpoczęcia pracy w formacie dd.mm.yyyy: '), '%d.%m.%Y')
end_date = datetime.strptime(input('Podaj datę zakończenia pracy w formacie dd.mm.yyyy: '), '%d.%m.%Y')
md = int(input('Podaj swoją stawkę za dzień pracy: '))

days = {}   # lib dict()
print(type(days))

while start_date <= end_date:
    print(start_date.strftime('%d.%m.%Y'))
    start_date += timedelta(days=1)
    days[start_date.strftime('%a')] = days.get(start_date.strftime('%a'), 0) + 1

work_day = 0
week_day = 0

for dd, occur in days.items():
    if dd in ('Sat','Sun'):
        week_day += occur
    else:
        work_day += occur

print(f'Twoja wypłata to: {work_day * md + week_day * md * 2}')
