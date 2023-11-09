def calculate_greater_divisor(fn: int, sn: int, min_num=2):
    list_of_div = []
    for i in range(min_num, min(fn, sn) + 1):
        if fn % i == 0 and sn % i == 0 and i > min_num:
            list_of_div.append(i)

    return max(list_of_div) if len(list_of_div) > 0 else None


def test_calculate_greater_divisor():
    a = 6
    b = 12

    value = calculate_greater_divisor(a, b)

    assert value == 6

def test_calculate_greater_divisor_does_not_exists():
    a = 5
    b = 12

    value = calculate_greater_divisor(a, b)

    assert value is None
