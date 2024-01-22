def appearances(s, low, high):
    if low > high:
        return {}
    else:
        frequency = appearances(s, low+1, high)
        if s[low] in frequency:
            frequency[s[low]] += 1
        else:
            frequency[s[low]] = 1
        return frequency

