a = float(input()) * 2
b = float(input())
c = float(input())
d = b * b - 2 * a * c
if d > 0:
    d = d**0.5 / a
    b = b / a
    x1 = 0 - b - d
    x2 = d - b
    if x1 > x2:
        print(x2, x1)
    else:
        print(x1, x2)
elif d == 0:
    print(0 - b / a)
