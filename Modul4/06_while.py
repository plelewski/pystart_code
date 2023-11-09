numbers = []

while len(numbers) < 10:
    answer = int(input('Podaj liczbę dodatnią: '))
    if answer > 0:
        numbers.append(answer)

print(numbers)
print(f'najmniejsza liczba {min(numbers)} oraz największa {max(numbers)}')
