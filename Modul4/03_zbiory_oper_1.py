# collect_3 = set()
# collect_5 = set()
# for i in range(1,101):
#     if i % 3 == 0:
#         collect_3.add(i)
#     if i % 5 == 0:
#         collect_5.add(i)

collect_3 = set(range(3,101,3))
collect_5 = set(range(5,101,5))


print(collect_3)
print(collect_5)

collect_common = collect_3 & collect_5

print(collect_common)
