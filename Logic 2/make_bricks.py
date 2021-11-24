def make_bricks(small, big, goal):
    if big == 0 and goal > small:
        return False

    sisa = goal-big*5
    while sisa < 0:
        big -= 1
        sisa = goal-big*5
    if small >= sisa:
        return True
    else:
        return False


print(make_bricks(3, 1, 8), 'True')
print(make_bricks(3, 1, 9), 'False')
print(make_bricks(3, 2, 10), 'True')
print(make_bricks(3, 2, 8), 'True')
print(make_bricks(3, 2, 9), 'False')
print(make_bricks(6, 1, 11), 'True')
print(make_bricks(6, 0, 11), 'False')
print(make_bricks(1, 4, 11), 'True')
print(make_bricks(0, 3, 10), 'True')
print(make_bricks(1, 4, 12), 'False')
print(make_bricks(3, 1, 7), 'True')
print(make_bricks(1, 1, 7), 'False')
print(make_bricks(2, 1, 7), 'True')
print(make_bricks(7, 1, 11), 'True')
print(make_bricks(7, 1, 8), 'True')
print(make_bricks(7, 1, 13), 'False')
print(make_bricks(43, 1, 46), 'True')
print(make_bricks(40, 1, 46), 'False')
print(make_bricks(40, 2, 47), 'True')
print(make_bricks(40, 2, 50), 'True')
print(make_bricks(40, 2, 52), 'False')
print(make_bricks(22, 2, 33), 'False')
print(make_bricks(0, 2, 10), 'True')
print(make_bricks(1000000, 1000, 1000100), 'True')
print(make_bricks(2, 1000000, 100003), 'False')
print(make_bricks(20, 0, 19), 'True')
print(make_bricks(20, 0, 21), 'False')
print(make_bricks(20, 4, 51), 'False')
print(make_bricks(20, 4, 39), 'True')
