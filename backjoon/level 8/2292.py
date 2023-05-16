n = int(input())

num = 1    # 벌집의 개수
count = 1
while n > num :
  num += 6 * count    # 6의 배수로 증가하는 벌집
  count += 1    # 반복문 반복 횟수

print(count)
