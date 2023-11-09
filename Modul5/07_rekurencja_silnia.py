def silnia(num) -> int:
    """
    This function returns power from the num
    :param num: specific number
    :return: final value
    """
    if num == 1:
        return 1

    return num * silnia(num - 1)

print(silnia(5))
