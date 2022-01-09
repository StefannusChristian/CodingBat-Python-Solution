def front_back(string):
    if len(string) == 1:
        return string
    if len(string) == 0:
        return ''
    string = [i for i in string]
    a = string[0]
    b = string[-1]
    string.remove(a)
    string.remove(b)
    string.insert(0, b)
    string.append(a)
    return ''.join(string)
