def IsPointInCircle(x, y, xc, yc, r):
    return (x - xc)**2 + (y - yc)**2 <= r**2


r = IsPointInCircle(float(input()), float(input()),
                    float(input()), float(input()), float(input()))
print('YES' * r + 'NO' * (not r))
