def add_lists(list1: list, list2: list) -> list:
    out_list = []
    for x, y in zip(list1, list2):
        out_list.append(x + y)

    return out_list
