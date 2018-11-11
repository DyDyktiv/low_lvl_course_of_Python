n = int(input())
print((n * '+___ ')[:-1],
      ' '.join(f'|{i} /' for i in range(1, n + 1)),
      (n * '|__\ ')[:-1],
      (n * '|    ')[:-1], sep='\n')
