def sample(a, b, *args, **kwargs):
    print('a ',a)
    print('b ',b)
    print('args ', args)
    print('kwargs', kwargs)

sample(2, 3)
print('*****')
sample(2, 3, 5, 67, 68, 69, 70)
print('*****')
sample(2, 3, 5, 67, 68, x=69, y=70)
