def sum_above_limit(*args, limit:int = 0) -> int:
    output = 0
    print('limit ',limit)
    print('args', args)
    for i in args:
        if i > limit:
            output += i

    return output

print(sum_above_limit(1, 2, 4, 6, 7, 7, limit=5))
