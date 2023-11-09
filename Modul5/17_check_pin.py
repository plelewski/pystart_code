def check_pin(pin: str) -> bool:
    if not len(pin) == 4:
        return False

    for char in pin:
        if not char.isnumeric():
            return False

    return True


print(check_pin('1234'))
print(check_pin('123'))
print(check_pin('123a'))
