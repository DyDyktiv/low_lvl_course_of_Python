a = int(input())
b = int(input())
print(((a // b) // (-a - b) + 1) * b +
      ((b // a) // (-a - b) + 1) * a +
      (a // b) * (b // a) * a)
