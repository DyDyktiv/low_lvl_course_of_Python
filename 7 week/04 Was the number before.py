arr = list(map(int, input().split()))
bef = set()
for a in arr:
    if a in bef:
        print('YES')
    else:
        print('NO')
        bef.add(a)
