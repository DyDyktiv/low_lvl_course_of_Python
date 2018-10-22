n = int(input())
c = 1
m = 1
f = n
while n != 0:
    n = int(input())
    if f == n:
        c += 1
    else:
        if c > m:
            m = c
        c, f = 1, n
print(m)
