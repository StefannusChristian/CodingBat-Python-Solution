def near_hundred(n):
    jarak_100 = abs(n-100)
    jarak_200 = abs(n-200)
    if jarak_100 <= 10 or jarak_200 <= 10:
        return True
    return False
