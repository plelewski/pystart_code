
collect = []

for _ in range(5):
    answer = input('Podaj adres email: ')
    if (answer.endswith('.pl') or answer.endswith('.com')) and '@' in answer:
        collect.append(answer)

print(collect)
collect = set(collect)
print(collect)
