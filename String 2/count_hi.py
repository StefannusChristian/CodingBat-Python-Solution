def count_hi(string):
    count = 0
    for i in range(len(string)):
        if string[i:i+2] == 'hi':
            count += 1
    return count
