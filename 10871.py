# An integer A and an integer X are given. 
# It is a program that outputs all numbers smaller than X in A.
n, x = map(int, input().split())
l = list(map(int, input().split()))
for i in range(n):
  if l[i] < x :
    print(l[i], end=' ')