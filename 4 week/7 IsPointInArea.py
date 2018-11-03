def IsPointInArea(x, y):
    return ((x + 1)**2 + (y - 1)**2 <= 4 and 2 * x + 2 <= y and -x <= y) or \
           ((x + 1)**2 + (y - 1)**2 >= 4 and 2 * x + 2 >= y and -x >= y)


r = IsPointInArea(float(input()), float(input()))
print('YES' * r + 'NO' * (not r))
