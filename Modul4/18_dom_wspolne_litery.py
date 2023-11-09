answer1 = input('Podaj pierwsze słowo: ')
answer2 = input('Podaj drugie słowo: ')

ans1 = set(answer1.lower())
ans2 = set(answer2.lower())

collect_common = ans1 & ans2
print(collect_common)
