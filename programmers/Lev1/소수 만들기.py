from itertools import combinations
def solution(nums):
    answer = 0
    combi = list(combinations(nums, 3))
    tmp = []
    for i in combi :
        tmp.append(sum(i))
    for i in tmp :
        flag = True     # 소수 판별용
        for j in range(2, int(i**0.5)+1) :
            if i % j == 0 :
                flag = False
        if flag == True :
            answer += 1
    return answer