free, peps = tuple(map(int, input().split()))
sizes = sorted(list(map(lambda c: int(input()), range(peps))))
size = 0
for i, s in enumerate(sizes):
    upup = size + s
    if upup > free:
        print(i)
        break
    else:
        size = upup
else:
    print(peps)
