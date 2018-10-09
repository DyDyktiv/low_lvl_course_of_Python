a = int(input())
b = int(input())
print(((a % b) // (-a - b) + 1) * 'YES' +
      ((a % b) // (-a - b) + 2) % 2 * 'NO')
