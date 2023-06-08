def solution(s):
    answer = ''
    temp = s.split(' ', -1)
    for i in temp :
        for j in range(len(i)) :
            if j % 2 == 0 :
                answer += i[j].upper()
            else : answer += i[j].lower()
        answer += ' '
    return answer[0:-1]