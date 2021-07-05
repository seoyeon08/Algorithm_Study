# 알람시계 출력 프로그램이다.

h, m = input().split()  # 시, 분을 각각 입력받아 h, m에 저장
h = int(h)
m = int(m)

if m < 45 :
  h -= 1
  m = (60 + m) - 45
else :
  m = m - 45
if h < 0 :
  h += 24
print(h, m)