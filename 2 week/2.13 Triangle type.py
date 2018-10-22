a = int(input())
b = int(input())
c = int(input())

if a < b + c and b < a + c and c < a + b:
    event1 = a**2 + b**2 - c**2
    event2 = b**2 + c**2 - a**2
    event3 = c**2 + a**2 - b**2
    if event1 < 0 or event2 < 0 or event3 < 0:
        print('obtuse')
    elif event1 == 0 or event2 == 0 or event3 == 0:
        print('rectangular')
    else:
        print('acute')
else:
    print('impossible')
