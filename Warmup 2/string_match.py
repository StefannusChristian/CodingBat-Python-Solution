def string_match(a, b):
    if len(a) < 2 or len(b) < 2:
        return 0

    if len(a) > len(b):
        sisa = len(a) - len(b)
        a = a[:len(a)-sisa]
    elif len(b) > len(a):
        sisa = len(b) - len(a)
        b = b[:len(b)-sisa]

    count = 0
    for i in range(len(a)-2):
        if a[i:i+2] == b[i:i+2]:
            count += 1

    if (a[-2:] == b[-2:]):
        count += 1

    return count


print(string_match('xxcaazz', 'xxbaaz'))
# print(string_match('abc', 'abc'))
# print(string_match('abc', 'axc'))
# print(string_match('h', 'hello'))
