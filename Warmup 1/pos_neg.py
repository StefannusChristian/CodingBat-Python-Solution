def pos_neg(a, b, negative):
    if negative:
        if a < 0 and b < 0:
            return True
        else:
            return False
    else:
        if a < 0 and b >= 0:
            return True
        elif a >= 0 and b < 0:
            return True
        else:
            return False
