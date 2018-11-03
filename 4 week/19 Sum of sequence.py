def sumSequence(s):
    new = int(input())
    if new:
        return sumSequence(s + new)
    else:
        return s


print(sumSequence(0))
