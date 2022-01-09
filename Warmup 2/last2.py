def last2(string):
    if len(string) < 2:
        return 0
    count = 0
    a = string[-1]
    b = string[-2]
    for i in range(len(string)-1):
        if string[i] == b and string[i+1] == a:
            count += 1
    return count - 1