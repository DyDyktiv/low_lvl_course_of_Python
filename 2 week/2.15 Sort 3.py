a, b, c = int(input()), int(input()), int(input())

if a > b:
    b, a = a, b
if b > c:
    b, c = c, b
if a > b:
    b, a = a, b
print(a, b, c)
