m = float('inf')
for c in input().split():
    c = int(c)
    if 0 < c < m:
        m = c
print(m)
