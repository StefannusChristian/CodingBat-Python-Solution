def make_out_word(out, word):
    a = out[:2]
    b = out[2:]
    hasil = a+word+b
    return hasil


print(make_out_word('<<>>', 'Yay'))
print(make_out_word('<<>>', 'WooHoo'))
print(make_out_word('[[]]', 'word'))
