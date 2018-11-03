def distance(xa, ya, xb, yb):
    return ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5


x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
x3, y3 = int(input()), int(input())

print(distance(x1, y1, x2, y2) +
      distance(x1, y1, x3, y2) +
      distance(x2, y2, x3, y3))
