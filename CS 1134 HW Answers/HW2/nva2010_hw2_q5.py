def split_parity(lst):
    odd_index = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            lst[i], lst[odd_index] = lst[odd_index], lst[i]
            odd_index += 1
    return lst
print(split_parity([2,3,5,6]))
