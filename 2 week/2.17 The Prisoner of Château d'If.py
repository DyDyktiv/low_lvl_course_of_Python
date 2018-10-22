a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())

if a > b:
    b, a = a, b
if b > c:
    b, c = c, b
if a > b:
    b, a = a, b

if d > e:
    d, e = e, d

if a <= d and b <= e:
    print('YES')
else:
    print('NO')
