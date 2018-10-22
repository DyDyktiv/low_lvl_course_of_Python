a = int(input()) % 2
b = int(input()) % 2
c = int(input()) % 2

if (not a or not b or not c) and (a or b or c):
    print('YES')
else:
    print('NO')
