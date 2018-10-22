n = int(input()) + 1
if n > 1:
    print(1, end='')
    i = 2
    while i < n:
        print('', i, end='')
        i *= 2
