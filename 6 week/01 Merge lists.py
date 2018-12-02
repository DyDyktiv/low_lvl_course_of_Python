def merge(arr1, arr2):
    i1, i2 = 0, 0
    c1, c2 = len(arr1), len(arr2)
    r = []
    while i1 < c1 and i2 < c2:
        if arr1[i1] < arr2[i2]:
            r.append(arr1[i1])
            i1 += 1
        else:
            r.append(arr2[i2])
            i2 += 1
    else:
        if i1 < c1:
            r.extend(arr1[i1:])
        else:
            r.extend(arr2[i2:])
    return r


print(*merge(list(map(int, input().split())), list(map(int, input().split()))))
