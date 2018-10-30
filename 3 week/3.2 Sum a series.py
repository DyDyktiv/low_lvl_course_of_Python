n, s = int(input()), 0
while n > 0:
    s += 1 / (n * n)
    n -= 1
print(s)
