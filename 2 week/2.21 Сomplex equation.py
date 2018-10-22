a, b, c, d = int(input()), int(input()), int(input()), int(input())

if a == b == 0:
    print('INF')
elif a == 0:
    print('NO')
elif ((-b) // a) * a + b == 0:
    r = (-b) // a
    if r*c + d != 0:
        if r > 0 and int(r ** 0.5) ** 2 == r:
            r = int(r ** 0.5)
            print(-r, r, sep='\n')
        else:
            print(r)
    else:
        print('NO')
else:
    print('NO')
