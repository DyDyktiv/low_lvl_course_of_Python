a = float(input())
b = float(input())
c = float(input())
if a == 0:
    if b == 0:
        if c == 0:
            print(3)
        else:
            print(0)
    else:
        print(1, -c / b)
else:
    d = b * b - 4 * a * c
    if d > 0:
        d = d ** 0.5
        x1 = (-d - b) / a / 2
        x2 = (d - b) / a / 2
        if x1 > x2:
            print(2, x2, x1)
        else:
            print(2, x1, x2)
    elif d == 0:
        print(1, -b / a / 2)
    else:
        print(0)
