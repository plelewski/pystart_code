# how many times the word exists in the sentence
sentence = 'raz dwa raz trzy'

how_many_times = dict()

# 1
# for word in sentence.split(' '):
#     if how_many_times.get(word) is None:
#         how_many_times[word] = 0
#
#     how_many_times[word] += 1

# 2
for word in sentence.split(' '):
    how_many_times[word] = how_many_times.get(word, 0) + 1

print(how_many_times)
