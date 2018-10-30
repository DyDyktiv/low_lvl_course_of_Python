s = input()
first = s.find('f')
if first != -1:
    entry = s.find('f', first + 1)
    if first != entry:
        print(entry)
    else:
        print(-1)
else:
    print(-2)
