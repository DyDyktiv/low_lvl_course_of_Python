n = int(input())
s = 0
f = 0
while n != 0:
    if n > f:
        if f > s:
            s = f
        f = n
    elif n > s:
        s = n
    n = int(input())
print(s)
