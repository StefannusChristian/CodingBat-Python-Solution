def count_dog(string):
    n = len(string)
    count = 0
    for i in range(n):
        if string[i:i+3] == 'dog':
            count += 1
    return count

def count_cat(string):
    n = len(string)
    count = 0
    for i in range(n):
        if string[i:i+3] == 'cat':
            count += 1
    return count

def cat_dog(string):
    dog = count_dog(string)
    cat = count_cat(string)
    if dog == cat:
        return True
    return False
