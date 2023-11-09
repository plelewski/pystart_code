def give_oposite(numbers: list) -> list:
    output = []
    for i in numbers:
        output.append(i * -1)

    return output


print(give_oposite([2, 4, -3]))
