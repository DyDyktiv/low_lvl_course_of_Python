square = 0
linear = 0
n = -1
new = -1
while new != 0:
    new = int(input())
    square += new * new
    linear += new
    n += 1
print(((square - linear * linear / n) / (n - 1))**0.5)
