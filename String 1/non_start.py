def non_start(a, b):
    a = a.replace(a[0], '')
    b = b.replace(b[0], '')
    return a+b


print(non_start('Hello', 'There'))
print(non_start('java', 'code'))
print(non_start('shotl', 'java'))
