a = int(input())
b = int(input())
c = int(input())
result_list = list(str(a * b * c))
for i in range(10) :
  print(result_list.count(str(i)))