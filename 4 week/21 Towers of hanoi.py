def move(n, x, y):
    before = 6 - x - y
    if n == 1:
        print(n, x, y)
    else:
        move(n - 1, x, before)
        print(n, x, y)
        move(n - 1, before, y)


move(int(input()), 1, 3)
