#시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 
# 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램이다.

def score_p (s) : 

  if s < 0 or s > 100 :
    return("Error")

  elif s >= 90 :
    return ("A")

  elif s >= 80 :
    return ("B")

  elif s >= 70 :
    return ("C")

  elif s >= 60 :
    return ("D")

  else :
    return ("F")

score = int(input())    # 시험 점수를 입력받는다
print(score_p(score))   # 점수 별 등급을 출력한다
