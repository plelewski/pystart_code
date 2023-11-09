from datetime import date, timedelta, datetime

#####
today = date.today()
formatted = today.strftime("%d.%m.%Y")
print(today)
print(type(formatted))
print(formatted)

day = date(today.year, 11, 9)
formatted2 = day.strftime("%d.%m.%Y")
print(formatted2)

#####
diff = timedelta(days=7)
print(diff)
end = today + diff
print(end)

#####
event = datetime.now()
print(event.hour)
print(event.minute)
print(event.strftime('%H:%M'))
