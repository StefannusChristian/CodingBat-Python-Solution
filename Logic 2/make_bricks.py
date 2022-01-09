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
