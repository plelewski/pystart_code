def count_signs(text:str, char_start:str = '(', char_end:str = ')') -> int:
    how_many_signs = 0
    counting = False

    for sign in text:
        if sign == char_start:
            counting = True
        elif sign == char_end:
            counting = False
        else:
            if counting:
                how_many_signs += 1

    return how_many_signs

def test_count_signs():
    value_1 = count_signs('(ala) ma (kota)')
    value_2 = count_signs('<> kod <103>', '<', '>')
    value_3 = count_signs('abrakadabra')

    assert value_1 == 7
    assert value_2 == 3
    assert value_3 == 0
