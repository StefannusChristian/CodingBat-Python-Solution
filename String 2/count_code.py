def count_code(string):
    count = 0
    for i in range(len(string)):
        code = string[i:i+4]
        if code[:2] == 'co' and code[-1] == 'e':
            count += 1
    return count
