def IsPrime(n):
    if n % 2 == 0:
        if n == 2:
            return True
        return False
    i = int(n**0.5)
    i = i + int(not (i % 2))
    while i > 2:
        if n % i == 0:
            return False
        i -= 2
    return True


r = IsPrime(int(input()))
print('YES' * r + 'NO' * (not r))
