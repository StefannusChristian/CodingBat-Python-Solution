def weekday(n):
    day = [1, 2, 3, 4, 5]
    if n in day:
        return True
    return False


def alarm_clock(day, vacation):
    day = weekday(day)
    if vacation:
        if day:
            return '10:00'
        else:
            return 'off'
    else:
        if day:
            return '7:00'
        else:
            return '10:00'
