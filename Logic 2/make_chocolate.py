def make_chocolate(small, big, goal):
    b = big*5
    sisa = goal - b
    while sisa < 0:
        big -= 1
        sisa = goal-(big*5)
    if sisa > small:
        return -1
    else:
        return sisa
