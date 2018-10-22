startV = int(input())
startH = int(input())
endV = int(input())
endH = int(input())

if startV - 2 < endV < startV + 2 and startH - 2 < endH < startH + 2:
    print('YES')
else:
    print('NO')
