from datetime import datetime, date

today = date.today()
year = today.year

first_day_of_summer = date(year, 6, 21)

if today > first_day_of_summer:
    first_day_of_summer = date(year+1, 6, 21)

time_delta = first_day_of_summer - today
print(f'do 21 czerwca pozostało {time_delta.days} dni')
