n = int(input())
f = 0
while n != 0:
    if n > f:
        f = n
        c = 1
    elif n == f:
        c += 1
    n = int(input())
print(c)
