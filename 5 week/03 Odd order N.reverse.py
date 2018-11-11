order = int(input())
print(*tuple(range(10**order - 1, 10**(order - 1) - 1, -2)))
