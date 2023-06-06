def solution(s):
    answer = ''
    a = list(s)
    a.sort()
    a.reverse()
    answer = "".join(a)
    return answer