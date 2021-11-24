def round_sum(a, b, c):
    hasil = round10(a) + round10(b) + round10(c)
    return hasil


def round10(num):
    num = str(num)
    if len(num) == 1:
        num = int(num)
        if num == 5:
            return num+5
        elif num == 6:
            return num+4
        elif num == 7:
            return num+3
        elif num == 8:
            return num+2
        elif num == 9:
            return num+1
        else:
            return 0
    else:
        belakang = num[-1]
        belakang = int(belakang)
        num = int(num)
        if belakang == 5:
            return num+5
        elif belakang == 6:
            return num+4
        elif belakang == 7:
            return num+3
        elif belakang == 8:
            return num+2
        elif belakang == 9:
            return num+1
        elif belakang == 1:
            return num-1
        elif belakang == 2:
            return num-2
        elif belakang == 3:
            return num-3
        elif belakang == 4:
            return num-4
        elif belakang == 5:
            return num-5
        elif belakang == 0:
            return num


print(round_sum(16, 17, 18))
print(round_sum(12, 13, 14))
print(round_sum(6, 4, 4))
