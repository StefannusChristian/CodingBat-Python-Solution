def not_string(string):
    depan = string[:3]
    if depan == 'not':
        return string
    else:
        return 'not '+string
