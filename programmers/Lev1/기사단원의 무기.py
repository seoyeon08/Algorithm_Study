def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1) :
        cnt = 0
        for j in range(1, int(i**0.5)+1) :  # 제곱근까지만 돌리기
            if i % j == 0 :
                cnt += 1   
                if j != i//j :          # 제곱근 중복 방지
                    cnt += 1
        if cnt <= limit :
            answer += cnt
        else :
            answer += power
    return answer