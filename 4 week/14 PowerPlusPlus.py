def power(a, n):
    if n == 2:
        return a * a
    if n % 2:
        return power(a, n - 1) * a
    if n == 1:
        return a
    if n == 0:
        return 1
    return power(a**2, n // 2)


print(power(float(input()), int(input())))
