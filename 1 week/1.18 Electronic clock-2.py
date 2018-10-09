ss = int(input())
mm = ss // 60
ss = ss % 60
ss = str(ss // 10) + str(ss % 10)
h = mm // 60 % 24
mm = mm % 60
mm = str(mm // 10) + str(mm % 10)
print(h, mm, ss, sep=':')
