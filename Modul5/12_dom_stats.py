
def get_list_stats(my_list: list) -> dict:
    total = len(my_list)

    return {
        'total': total,
        'mean': sum(my_list)/total,
        'min': min(my_list),
        'max': max(my_list)
    }

stats = get_list_stats([1,4,33,5443,23,123,55])
print(stats)
