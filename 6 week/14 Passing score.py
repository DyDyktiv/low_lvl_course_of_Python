scores = []
with open('input.txt', 'r', encoding='utf-8') as f:
    k = int(f.readline()[:-1])
    for s in f:
        w = tuple(map(int, s.split()[2:]))
        if w[0] > 39 and w[1] > 39 and w[2] > 39:
            w = sum(w)

if len(scores) > k:
    pass
else:
    pass
