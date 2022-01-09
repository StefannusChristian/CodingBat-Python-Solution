def date_fashion(you, date):
    if you >= 8:
        if date > 2:
            return 2
        else:
            return 0
    if date >= 8:
        if you > 2:
            return 2
        else:
            return 0
    if (you < 8 and you > 2) and (date < 8 and date > 2):
        return 1
    if you <= 2 or date <= 2:
        return 0
