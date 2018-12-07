arr = list(set(map(int, input().split())) & set(map(int, input().split())))
print(*sorted(arr))
