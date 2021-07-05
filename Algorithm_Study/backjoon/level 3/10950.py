# The program takes two integers, A and B, and then outputs A+B.

n = int(input())
for i in range(n) :
  a, b = map(int, input().split())
  print(a+b)