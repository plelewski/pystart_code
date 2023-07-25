grades = (3, 6, 6, 5, 4, 5)

# sorted
print(sorted(grades))

# avg + 4.75
avg_grades = sum(grades) / len(grades)
if avg_grades >= 4.75:
    print(f'Masz czerwony pasek. Masz {avg_grades:.2f}')
else:
    print(f'Niestety nie masz czerwonego paska na świadectwie bo masz tylko {avg_grades:.2f}')
