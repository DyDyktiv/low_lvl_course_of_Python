n = int(input())
m = int(input())
k = int(input())

if m * n > k and ((k // n < m and k % n == 0) or (k // m < n and k % m == 0)):
    print('YES')
else:
    print('NO')
