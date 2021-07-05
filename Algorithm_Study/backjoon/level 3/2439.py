# print star 2
n = int(input())
for i in range(1, n+1):
  print(' ' * int(n-i) + '*' * i)