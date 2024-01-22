def flat_list(nested_lst, low, high):
    if low > high:
        return []
    flattened = []
    if type(nested_lst[low]) == list:
        flattened += flat_list(nested_lst[low], 0, len(nested_lst[low]) - 1)
    else:
        flattened.append(nested_lst[low])
    flattened += flat_list(nested_lst, low + 1, high)
    return flattened


