def get_most_popular_word(*args, ignore_case=True) -> list:
    list_of_words = dict()

    for word in args:
        word = word.lower() if ignore_case else word
        list_of_words[word] = list_of_words.get(word, 0) + 1

    max_num_of_occur = max(list_of_words.values())

    output = []
    for word, occurrences in list_of_words.items():
        if occurrences == max_num_of_occur:
            output.append(word)

    return output

print(get_most_popular_word('raz', 'dwa', 'trzy', 'raz', 'cztery', 'dwa'))
print(get_most_popular_word('raz', 'dwa', 'raz', 'trzy', 'AAA', 'aaa', 'aaa'))
print(get_most_popular_word('raz', 'dwa', 'raz', 'trzy', 'AAA', 'aaa', 'aaa', ignore_case=False))
