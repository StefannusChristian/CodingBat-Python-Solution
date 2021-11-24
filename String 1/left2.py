def left2(string):
    if len(string) == 2:
        return string
    dua = string[:2]
    string = string.replace(string[:2], '')
    return string+dua
