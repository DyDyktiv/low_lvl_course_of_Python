m = input().split()
last = int(m[0])
for c in m[1:]:
    c = int(c)
    if c > last:
        print(c, end=' ')
    last = c
