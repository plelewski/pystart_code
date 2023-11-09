def convert_int_to_str(number:int) -> list:
    output = []
    for element in str(number):
        output.append(element)

    return output

def sort_digits(number: int) -> str:
    list_of_ints = convert_int_to_str(number)
    list_of_ints.sort(reverse=True)

    return ''.join(list_of_ints)


print(sort_digits(12345))
