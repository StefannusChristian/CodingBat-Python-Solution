def near_ten(num):
    a = num + 2
    b = num - 2
    c = num + 1
    d = num - 1
    a, b, c, d = map(str, (a, b, c, d))
    num = str(num)
    if num[-1] == '0':
        return True
    if a[-1] == '0' or b[-1] == '0' or c[-1] == '0' or d[-1] == '0':
        return True
    return False


print(near_ten(12))
print(near_ten(17))
print(near_ten(19))
