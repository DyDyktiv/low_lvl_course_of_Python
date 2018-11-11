maximum, index, i = 0, 0, 0
for c in input().split():
    c = int(c)
    if c >= maximum:
        if c > maximum:
            maximum = c
        index = i
    i += 1
print(maximum, index)
