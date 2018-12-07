arr = set(i for i in range(1, int(input()) + 1))
while 1:
    s = input()
    if s == 'HELP':
        break
    else:
        a = input()
        if a == 'YES':
            arr.intersection_update(set(map(int, s.split())))
        else:
            arr.difference_update(set(map(int, s.split())))
print(*sorted(arr))
