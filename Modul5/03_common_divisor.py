def calculate_common_divisor(fn, sn, min_num=2):
    list_of_div = []
    for i in range(min_num, min(fn, sn) + 1):
        if fn % i == 0 and sn % i == 0 and i > min_num:
            list_of_div.append(i)

    return list_of_div


print(calculate_common_divisor(3, 6))
print(calculate_common_divisor(3, 6, 4))
print(calculate_common_divisor(16, 8))
