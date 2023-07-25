value = int(input('Podaj czas wyrażony w sekundach (< 86400): '))

if value >= 86400:
    print('ehhh miało być poniżej')
else:
    hour = value // 3600
    minute = (value - hour * 3600) // 60
    second = value - hour * 3600 - minute * 60

print(f'To jest godzina {hour:02d}:{minute:02d}:{second:02d}')
