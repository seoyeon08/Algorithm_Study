def solution(board, moves):
    answer = 0
    a = [0]    # 오류 방지
    temp = 0
    for i in moves :
        for j in board :
            if j[i-1] != 0 :
                if a[-1] == j[i-1] :    # stack top이랑 뽑은거랑 같으면
                    a.pop()             # top을 pop시키고 answer+2
                    answer += 2
                    j[i-1] = 0          # 결국 뽑은거니까 뽑은 자리는 0으로 바꿔주기
                else :
                    a.append(j[i-1])
                    j[i-1] = 0 
                break
    return answer