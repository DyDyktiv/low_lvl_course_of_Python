n, d = int(input()), 0
mf, mb = [], []
xrange = range(n)
while n > 0:
    f, b = input().split()
    b = int(b)
    for i in xrange[:d]:
        if mb[i] < b:
            mf.insert(i, f)
            mb.insert(i, b)
            break
    else:
        mf.append(f)
        mb.append(b)
    n -= 1
    d += 1
print('\n'.join(mf))
