amount = int(input())
m = tuple(map(int, input().split()[: amount]))
n = int(input())
delta = float('inf')
search = 0
for number in m:
    d = abs(n - number)
    if d:
        if d < delta:
            search = number
            delta = d
    else:
        print(number)
        break
else:
    print(search)
