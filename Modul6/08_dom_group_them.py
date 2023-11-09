def group_them(**kwargs) -> list:
    output = []
    for k,v in kwargs.items():
        output.append(f'{k.title()} is {v}')

    return '\n'.join(output)

def test_group_them():
    assert group_them() == ''
    assert group_them(python='super', java='almost super') == 'Python is super\nJava is almost super'

if __name__ == '__main__':
    print(group_them(python='super', java='almost super'))

# python 08_dom_group_them
# python -m pytest 08_dom_group_them