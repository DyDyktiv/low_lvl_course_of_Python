x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x2 > x1:
    side = x2 - x1
else:
    side = x1 - x2

up = y2 - y1

if up > 0 and (x1 + y1) % 2 == 0 and (x2 + y2) % 2 == 0 and side <= up:
    print('YES')
else:
    print('NO')
