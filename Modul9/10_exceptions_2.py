
# w pierwszym pomimo exception odpytuje nadal
# w drugim przerywa działanie

fruits = []
# for _ in range(10):
#     answer = input('Jaki owoc dodać do listy? ')
#
#     try:
#         if answer in fruits:
#             raise ValueError('Owoc jest już na liście')
#         fruits.append(answer)
#
#     except ValueError as message:
#         print(message)
#
# print('good bye!')

try:
    for _ in range(10):
        answer = input('Jaki owoc dodać do listy? ')

        if answer in fruits:
            raise ValueError('Owoc jest już na liście')
        fruits.append(answer)

except ValueError as message:
    print(message)

print('good bye!')
