def xyz_there(string):
    string = string.replace('.xyz', '')
    if 'xyz' in string:
        return True
    return False
