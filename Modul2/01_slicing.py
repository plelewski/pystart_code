values = tuple(range(1,101))
# bez słowa tuple byłby type range i wtedy trzeba zastosować słowo kluczowe "list" przed zmienną values
# first 10
print(values[:10])

# last 10
print(values[-10:])

# even numbers
print(values[::2])

# odd numbers
print(values[::-2])
