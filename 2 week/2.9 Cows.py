cows = int(input())
if cows % 10 > 4 or cows % 10 == 0 or cows // 10 == 1:
    print(cows, 'korov')
elif 1 < cows % 10 < 5:
    print(cows, 'korovy')
else:
    print(cows, 'korova')
