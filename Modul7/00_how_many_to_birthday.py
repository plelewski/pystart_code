from datetime import date, datetime

today = date.today()
answer = input('Podaj dzień i miesiąc swoich urodzin w formacie dd-mm: ')
when_birthday = date(today.year, int(answer[-2:]), int(answer[:2]))

# parsowanie z daty jako przykład
when_birthday2 = datetime.strptime(answer, '%d-%m')
print(f'dzień: {when_birthday2.day}, miesiąc: {when_birthday2.month}')
# koniec przykładu

if today < when_birthday:
    diff = when_birthday - today
else:
    diff = date(today.year + 1, when_birthday.month, when_birthday.day) - today

print('Twoje urodziny będą ', (today + diff).strftime('%a, %d.%m.%Y'), f'. Do urodzin pozostało {diff.days} dni')
