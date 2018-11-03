def phib(oldold, old, n):
    if n == 0:
        return old
    return phib(old, old + oldold, n - 1)


p = int(input())
if p < 3:
    print(1)
else:
    print(phib(1, 1, p - 2))
