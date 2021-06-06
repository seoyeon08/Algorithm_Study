arr = []
for i in range(10):
  n = int(input())
  arr.append(n%42)
arr = set(arr)      # set에는 중복이 없다~
print(len(arr))