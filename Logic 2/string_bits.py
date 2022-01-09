def string_bits(string):
    hasil = ''
    diambil = [i for i in range(0, len(string), 2)]
    for i in diambil:
        hasil += string[i]
    return hasil
    
