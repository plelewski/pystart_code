base_salary = 2000
total = base_salary

seniority = int(input('Ile pełnych lat masz przepracowane? '))
hours_in_month = int(input('Ile godzin przepracował pracownik w miesiącu? '))
items_sold = int(input('Ile pracownik sprzedał towarów w miesiącu? '))

seniority_bonus = 0.1 if seniority > 2 else 0.02
bonus = 0.25 if items_sold >= 30 else 0
active = 0.08 if hours_in_month >= 160 else 0.02

print(f'Całkowite wynagrodzenie wynosi {round(total * (1 + seniority_bonus + bonus + active))}')
