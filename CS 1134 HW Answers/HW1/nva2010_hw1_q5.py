def fibs(n):
    add_end_1 = 0
    add_end_2 = 1
    for i in range(n):
        sum = add_end_1 + add_end_2
        add_end_1 = add_end_2
        yield add_end_2
        add_end_2 = sum

