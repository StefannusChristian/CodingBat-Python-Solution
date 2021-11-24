def missing_char(string, n):
    string = string.replace(string[n], '')
    return string


print(missing_char('kitten', 1))
