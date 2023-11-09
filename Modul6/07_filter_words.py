def filter_words(sent: str) -> list:
    output = []
    vowels = 'aąeęiou'
    words = list(sent.split(' '))
    for word in words:
        if word[:1] not in vowels and word[-1:] in vowels:
            output.append(word)

    return output if len(output) > 0 else None

def test_filter_words():
    assert isinstance(filter_words('ala ma kota'), list)
    assert filter_words('ala ma kota') == ['ma', 'kota']

def test_filter_words_empty():
    assert filter_words('ala ola ula') is None
