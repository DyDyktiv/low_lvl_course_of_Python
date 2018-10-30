s = input()
first = s.find('f')
if first != -1:
    entry = len(s) - s[::-1].find('f') - 1
    if first != entry:
        print(first, entry)
    else:
        print(first)
