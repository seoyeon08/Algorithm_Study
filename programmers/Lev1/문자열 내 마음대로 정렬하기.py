def solution(strings, n):
    answer = []
    temp = []
    for i in strings :
        temp.append(i[n]+i)
    temp.sort()
    for j in temp :
        answer.append(j[1:])
    return answer