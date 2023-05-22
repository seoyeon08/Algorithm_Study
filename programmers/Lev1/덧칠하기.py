def solution(n, m, section):  
    answer = 0
    index = section[0]-1
    if m == 1 : return len(section)                 # m이 1이면 어쩔 수 없음
    elif section[-1] - section[0] < m : return 1     # 한 번에 칠할 수 있는 범위 내
    # 그럼 한 번에 칠하지 못할 때는
    else :
        for i in section :
            if index < i :
                index = i + m - 1
                answer += 1
        return answer
