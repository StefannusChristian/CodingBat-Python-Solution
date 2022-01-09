def without_end(string):
    s = [i for i in string]
    s.pop(0)
    s.pop(len(s)-1)
    hasil = ''.join(s)
    return hasil