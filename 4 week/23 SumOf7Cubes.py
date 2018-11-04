def rec(number, n=6):
    base = int(number**(1/3))
    delta = number - base**3
    if delta == 0:
        print(base**3, end=' ')
        return True
    elif n > 0:
        while base > 0:
            r = rec(delta, n - 1)
            if r:
                print(base**3, end=' ')
                return True
            else:
                base -= 1
                delta = number - base**3
        return False
    return False


ret = rec(int(input()))
if not ret:
    print(0)
else:
    print()
