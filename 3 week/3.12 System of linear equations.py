kx1 = float(input())
ky1 = float(input())
kx2 = float(input())
ky2 = float(input())
re1 = float(input())
re2 = float(input())

if kx1 == 0:
    y = re1 / ky1
    x = (re2 - ky2 * y) / kx2
elif ky1 == 0:
    x = re1 / kx1
    y = (re2 - kx2 * x) / ky2
elif kx2 == 0:
    y = re2 / ky2
    x = (re1 - ky1 * y) / kx1
elif ky2 == 0:
    x = re2 / kx2
    y = (re1 - kx1 * x) / ky1
else:
    x = (re2 - ky2 * re1 / ky1) / (kx2 - ky2 * kx1 / ky1)
    y = re1 / ky1 - kx1 / ky1 * x
print(x, y)
