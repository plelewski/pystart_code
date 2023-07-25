# divided by 4 and 5
numbers = (17, 20, 25, 100)

for num in numbers:
    if num % 4 == 0 and num % 5 == 0:
        print(f'Liczba {num} jest podzielna przez 4 i 5')

# names longer than 5 signs
names = ('Ala', 'Aleksandra', 'Przemek')

for name in names:
    if len(name) > 5:
        print(name)

# triangle based on numbers
for num1 in range(1,5):
    for num2 in range(1,6-num1):
        print(num2, end=' ')
    print()
