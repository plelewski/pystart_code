def get_divisors(n: int, m:int, z:int):
    values = []
    for value in range(n, m + 1):
        if value % z == 0:
            values.append(value)

    return values


def test_get_divisors():
    assert isinstance(get_divisors(2, 10, 2), list)
    assert get_divisors(2, 10, 2) == [2, 4, 6, 8, 10]
    assert get_divisors(3, 12, 2) == [4, 6, 8, 10, 12]
    assert get_divisors(2, 10, 30) == []
