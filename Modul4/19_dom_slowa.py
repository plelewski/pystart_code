answer = input('Podaj listę słów oddzielonych przecinkami: ')

answer_list = set(answer.split(','))

for word in answer_list:
    print(word)
