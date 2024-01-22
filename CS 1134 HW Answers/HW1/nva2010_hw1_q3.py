# Question a
def sum_of_squares(n):
    sum = 0
    for i in range(n):
        sum += i ** 2
    return sum
# Question b
sum([i**2 for i in range(n)])
# Question c
def sum_of_odd_squares(n):
    sum = 0
    for i in range(n):
        if i % 2 == 1:
            sum += i ** 2
    return sum
# Question d
sum([i**2 for i in range(n) if i % 2 == 1])

