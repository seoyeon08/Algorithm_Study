# input integer a, b & print a+b
t = int(input())
for i in range(t):
  a,b = map(int, input().split())
  print('Case #%d:'%(i+1), a+b)