def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if len(a) > len(b):
        if b == a[-len(b):]:
            return True
    elif len(b) > len(a):
        if a == b[-len(a):]:
            return True
    else:
        if a == b:
            return True
    return False

