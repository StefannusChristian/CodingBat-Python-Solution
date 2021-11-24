def xyz_there(string):
    while '.xyz' in string:
        string = string.replace('.xyz', '')

    if 'xyz' in string:
        return True
    return False
