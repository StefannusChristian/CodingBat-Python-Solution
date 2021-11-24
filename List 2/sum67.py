def sum67(arr):
    add = True
    count = 0
    for i in arr:
        if i == 6:
            add = False
        elif not add and i == 7:
            add = True
        elif add:
            count += i

    return count
