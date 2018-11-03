def only2():
    new = int(input())
    if new != 0:
        r = only2()
        if int(new**0.5)**2 == new:
            print(f' {new}', end='')
            return True
        else:
            return r
    else:
        return False


b = only2()
if not b:
    print(0)
