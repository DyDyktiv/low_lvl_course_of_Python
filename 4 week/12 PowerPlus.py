def power(a, n):
    if n >= 0:
        p = n
        r = 1
        while p:
            r *= a
            p -= 1
        return r
    else:
        p = -n
        r = 1
        while p:
            r *= a
            p -= 1
        return 1 / r


print(power(float(input()), int(input())))
