def solution(s):
    tmp = len(s)//2
    if len(s) % 2 == 0 :
        return str(s[tmp-1])+str(s[tmp])
    else :
        return str(s[tmp])