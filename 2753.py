# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램

def is_Leap(y) :                # 윤년 판별 함수
  if y%4 == 0 and y%100 != 0 :
    return("1")
  elif y%400 == 0 :
    return("1")
  else :
    return("0")

year = int(input())     # 연도를 입력 받고
print(is_Leap(year))    # 판별 결과를 출력한다.