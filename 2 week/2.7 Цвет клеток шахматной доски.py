startV = int(input())
startH = int(input())
endV = int(input())
endH = int(input())

if (startH + startV - endH - endV) % 2:
    print('NO')
else:
    print('YES')
