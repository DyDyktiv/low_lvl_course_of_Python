def Sum(a, b):
    if b > 0:
        return Sum(a + 1, b - 1)
    else:
        return a


print(Sum(int(input()), int(input())))
