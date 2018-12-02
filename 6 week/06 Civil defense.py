def reso():
    input()
    return sorted(list(enumerate(map(int, input().split()))),
                  key=lambda x: x[1])


hamlets, bunkers = reso(), reso()
r = [i for i in range(len(hamlets))]
down = 0
up = range(len(bunkers))
for h in hamlets:
    delta = abs(h[1] - bunkers[down][1])
    if delta:
        for i in up[down + 1:]:
            d = abs(h[1] - bunkers[i][1])
            if delta > d:
                delta = d
            else:
                down = i - 1
                r[h[0]] = bunkers[i - 1][0] + 1
                break
        else:
            r[h[0]] = bunkers[-1][0] + 1
    else:
        r[h[0]] = bunkers[down][0] + 1

print(*r)
