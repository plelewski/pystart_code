def reverse_sentence(sentence: str) -> str:
    words = []
    for word in sentence.split(' '):
        words.append(word[::-1])

    return ' '.join(words)


print(reverse_sentence('Ala ma kota'))
