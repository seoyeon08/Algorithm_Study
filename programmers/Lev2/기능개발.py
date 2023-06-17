import math
def solution(progresses, speeds):
    answer = []
    temp = []
    release = 1
    for i in range(len(progresses)) :
        temp.append(math.ceil((100-progresses[i])/speeds[i]))   # 남은 작업 수
    a = temp[0]
    for i in range(1, len(temp)) :
        if a < temp[i] :
            a = temp[i]
            answer.append(release)
            release = 1
        else :
            release += 1
    answer.append(release)
    return answer