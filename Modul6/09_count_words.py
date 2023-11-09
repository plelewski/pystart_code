
def count_words(sentence: str, word_to_find: str) -> int:
    result = 0

    for i in sentence.split(' '):
        if i == word_to_find:
            result += 1

    return result


def test_count_words():
    assert count_words('Python i Python', 'Python') == 2
    assert count_words('', 'Oko') == 0
