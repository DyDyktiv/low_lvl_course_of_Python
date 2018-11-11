start, end = int(input()), int(input())
if start <= end:
    print(*tuple(range(start, end + 1, 1)))
else:
    print(*tuple(range(start, end - 1, -1)))
