def filter_words(to_filter:list, min_len: int = 4, max_len: int = 8) -> list:
    """

    :param to_filter: list of words to filter
    :param min_len: minimum length for a single work
    :param max_len: maximum length for a single word
    :return: list of filter words
    """
    output = []
    for word in to_filter:
        if min_len <= len(word) <= max_len:
            output.append(word)

    return output


words_list = ['oko', 'ucho', 'noga', 'chrabąszcz']

print(filter_words(words_list))
