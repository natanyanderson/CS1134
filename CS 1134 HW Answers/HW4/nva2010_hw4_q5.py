def count_lowercase(s, low, high):
    if low > high:
        return 0
    if s[low].islower():
        return 1 + count_lowercase(s, low+1, high)
    else:
        return count_lowercase(s, low+1, high)

def is_number_of_lowercase_even(s, low, high):
    if low > high:
        return True
    else:
        if s[low].islower():
            return not is_number_of_lowercase_even(s, low + 1, high)
        else:
            return is_number_of_lowercase_even(s, low + 1, high)