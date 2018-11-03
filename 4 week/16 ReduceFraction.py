def ReduceFraction(n, m):
    if m % n == 0:
        return 1, m // n
    if n % 2 == m % 2 == 0:
        n, m = ReduceFractionTwice(n // 2, m // 2)
    return ReduceFractionOther(n, m)


def ReduceFractionTwice(n, m):
    if n % 2 == m % 2 == 0:
        return ReduceFractionTwice(n // 2, m // 2)
    else:
        return n, m


def ReduceFractionOther(n, m):
    i = n // 2
    i = i + int(not (i % 2))
    while i > 2:
        if n % i == m % i == 0:
            n, m = n // i, m // i
        i -= 2
    return n, m


p, q = int(input()), int(input())
if p > q:
    q, p = ReduceFraction(q, p)
else:
    p, q = ReduceFraction(p, q)
print(p, q)
