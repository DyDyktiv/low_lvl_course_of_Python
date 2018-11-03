def reverse():
    new = int(input())
    if new:
        reverse()
    print(new)


reverse()
