n = int(input())
a = n // 1000 + 1
b = n // 100 % 10 + 1
c = n // 10 % 10 + 1
d = n % 10 + 1
print((a // d) * (d // a) * (b // c) * (c // b))
