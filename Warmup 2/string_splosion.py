def string_splosion(string):
    hasil = ''
    for i in range(len(string)):
        hasil += string[:i+1]
    return hasil

