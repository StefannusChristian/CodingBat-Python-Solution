def close_far(a, b, c):
    ab = abs(a-b)
    ac = abs(a-c)
    bc = abs(b-c)
    if (ab == 1 and ac == 1) or (ac == 1 and bc == 1) or (ab == 1 and bc == 1):
        return False
    return True
