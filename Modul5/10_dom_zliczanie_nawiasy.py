def count_signs(text:str, char_start:str = '(', char_end:str = ')') -> int:
    """
    functions returns number of signs between all brackets ()
    :param char_end:
    :param char_start:
    :param text: text to analyze
    :return: value
    """
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


print(count_signs("Ala ma (kota)"))
print(count_signs("(Ala) ma (kota)"))
