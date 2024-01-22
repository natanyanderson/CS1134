def permutations(lst, low, high):
    if low == high:
        return [[lst[low]]]
    perms = permutations(lst, low + 1, high)
    result = []
    num = lst[low]
    for p in perms:
        for i in range(len(p) + 1):
            p_copy = p[::]
            p_copy.insert(i, num)
            result.append(p_copy)
    return result


