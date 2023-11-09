def print_all(a, b, *others):
    print('a ',a)
    print('b ',b)
    print(others)

def save(filename, **kwargs):
    print(filename)
    print(kwargs)

print_all('oko', 'ucho', '1', '2', '3')
save('students.txt', first_name='Jacek', last_name='Placek')
