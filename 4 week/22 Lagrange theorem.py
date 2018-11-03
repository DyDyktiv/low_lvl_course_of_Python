def rec(number, n=3):
    base = int(number**0.5)
    square = base**2
    if square == number:
        print(base)
        return True
    elif n:
        r = rec(number - square, n - 1)
        if r:
            print(base)
            return True
        else:
            while base:
                base -= 1
                square = base**2
                r = rec(number - square, n - 1)
                if r:
                    print(base)
                    return True
            return False


rec(int(input()))
