def countSort(arr):
    counts = [0] * 101
    for c in arr:
        counts[int(c)] += 1
    arr = []
    for i, c in enumerate(counts):
        arr.extend([i] * c)
    return arr


print(*countSort(input().split()))
