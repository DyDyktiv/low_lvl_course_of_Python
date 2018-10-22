k = int(input())

if ((k % 5 % 3 == 0 or k % 5 % 3 == 1 or k % 5 % 3 == 2) and k > 10) or \
        k % 5 % 3 == 0:
    print('YES')
else:
    print('NO')
