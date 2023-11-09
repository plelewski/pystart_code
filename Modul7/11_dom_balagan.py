
correct_lines = []
with open('balagan.txt', encoding='utf8', mode='r') as file:
    for line in file:
        if 'Java Script' not in line:
            line = line.replace('Java', 'Python')

        correct_lines.append(line.strip())


with open('balagan1.txt', encoding='utf8', mode='w') as file:
    # file.writelines(correct_lines)    wszystko w jednym wierszu
    file.write('\n'.join(correct_lines))
