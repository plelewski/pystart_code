numbers = []
last_number = None

while True:
    answer = int(input(f'Podaj liczbę większą od {last_number}: '))
    if last_number is not None and answer <= last_number:
        break
    numbers.append(answer)
    last_number = answer

print(numbers)
print(f'średnia z liczb wynosi {sum(numbers) / len(numbers)}')
