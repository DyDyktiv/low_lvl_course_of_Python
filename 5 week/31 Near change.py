m = input().split()
for i in range(0, len(m) - 1, 2):
    m[i], m[i + 1] = m[i + 1], m[i]
print(*m)
