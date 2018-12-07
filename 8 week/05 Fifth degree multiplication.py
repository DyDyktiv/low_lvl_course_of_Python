from functools import reduce


print(reduce(lambda m, n: n * m, map(lambda n: int(n)**5, input().split())))
