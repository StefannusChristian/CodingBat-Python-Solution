def lucky_sum(a, b, c):
    if a == 13:
        return 0
    elif b == 13:
        return a
    elif c == 13:
        return a+b
    elif a == b == c == 13:
        return 0
    else:
        return a+b+c
