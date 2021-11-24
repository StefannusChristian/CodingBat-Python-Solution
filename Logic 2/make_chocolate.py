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


if __name__ == "__main__":
    print(make_chocolate(6, 2, 7))  # 2
    print(make_chocolate(4, 1, 5))  # 0
    print(make_chocolate(4, 1, 4))  # 4
