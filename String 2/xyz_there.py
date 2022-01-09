def xyz_there(string):
    # Erase all .xyz in string
    string = string.replace('.xyz', '')
    if 'xyz' in string:
        return True
    return False
