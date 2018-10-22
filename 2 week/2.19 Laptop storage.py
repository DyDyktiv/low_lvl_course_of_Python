a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())

maximum = (a1 // a2) * (b1 // b2) * (c1 // c2)
v = (a1 // a2) * (b1 // c2) * (c1 // b2)
if v > maximum:
    maximum = v
v = (a1 // b2) * (b1 // a2) * (c1 // c2)
if v > maximum:
    maximum = v
v = (a1 // b2) * (b1 // c2) * (c1 // a2)
if v > maximum:
    maximum = v
v = (a1 // c2) * (b1 // a2) * (c1 // b2)
if v > maximum:
    maximum = v
v = (a1 // c2) * (b1 // b2) * (c1 // a2)
if v > maximum:
    maximum = v

print(maximum)
