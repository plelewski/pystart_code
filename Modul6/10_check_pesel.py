
def check_pesel(pesel: str, control:str = '13791379131') -> bool:
    total = 0
    if len(pesel) != 11:
        return False

    for pesel_digit, pesel_control in zip(pesel, control):
        total += int(pesel_digit) * int(pesel_control)

    if total & 10 != 0:
        return False

    return True


def test_check_pesel():
    assert not check_pesel('123', '13791379131') # inny sposób zapisu poniższego
    assert check_pesel('12345678912', '13791379131') is False
    assert check_pesel('77022402453', '13791379131') is True


if __name__ == '__main__':
    print(check_pesel('2343', ))
