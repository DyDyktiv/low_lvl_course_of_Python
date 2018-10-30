percent = int(input()) + 100
deposid = int(input()) * 100 + int(input())
years = int(input())
while years:
    deposid = deposid * percent // 100
    years -= 1
print(deposid // 100, deposid % 100)
