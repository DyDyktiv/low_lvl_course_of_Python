x = int(input())
y = int(input())

if not (x - 1) % (y - x + 1):
    print('YES')
else:
    print('NO')
