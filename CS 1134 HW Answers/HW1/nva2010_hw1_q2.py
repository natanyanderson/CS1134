def shift(lst, k, direction="left"):
    if direction == "left":
        for ind in range(k):
            lst.append(lst.pop(0))
    elif direction == "right":
        for ind in range(k):
            lst.insert(0,lst.pop(-1))
    return lst


