n = int(input())
i = 0
if n != 0:
    k, n = n, int(input())
    while n != 0:
        if k < n:
            i += 1
        k, n = n, int(input())
print(i)
