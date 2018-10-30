s = input()
first = s.find('h')
entry = len(s) - s[::-1].find('h')
print(s[:first] + s[entry:])
