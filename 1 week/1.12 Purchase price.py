price_rub = int(input())
price_kop = int(input())
pies = int(input())
print(price_rub * pies + price_kop * pies // 100, price_kop * pies % 100)
