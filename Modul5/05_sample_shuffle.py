from random import sample,shuffle

ttt = '123456'
print(ttt)
print(sample(ttt, 3))

words = ['laptop', 'pajacyk', 'rzeka', 'robak', 'parapet']
print(sample(words, 3))
shuffle(words)
print(words)
