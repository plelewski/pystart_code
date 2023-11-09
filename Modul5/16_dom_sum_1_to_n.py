# def sum_all(num: int) -> int:
#     output = 0
#     for i in range(1, num + 1):
#         output += i
#
#     return output

def sum_all(num: int) -> int:
    if num == 0:
        return 0
    return num + sum_all(num - 1)

print(sum_all(5))
