def write_text(text, delimiter=',', repeat=1):
    output = []
    for _ in range(0, repeat):
        output.append(text)

    return delimiter.join(output)


print(write_text('Ala ma kota'))
print(write_text('Python', delimiter=';', repeat=3))
