def front_times(string, n):
    if len(string) < 3:
        return string*n
    else:
        return string[:3]*n
