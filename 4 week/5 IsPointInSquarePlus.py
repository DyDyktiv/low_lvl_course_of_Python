def IsPointInSquare(x, y):
    return -1 <= abs(x) + abs(y) <= 1


r = IsPointInSquare(float(input()), float(input()))
print('YES' * r + 'NO' * (not r))
