def solution(n):
    answer = 0
    n = n ** (0.5)
    if n % 1 == 0 :
        answer = (n+1) ** 2
    else :
        answer = -1
    return answer