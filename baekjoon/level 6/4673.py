def d(n):
  n=n+sum(map(int,str(n)))
  return n

#리스트 초기화
a=[0]*10001

#생성자 찾기
for i in range(1,10001):
  a[i]=d(i)

for i in range(1,10001):
  #셀프넘버이면, 출력
  if i not in a:
    print(i)