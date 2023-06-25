def binaryNum(n, tmp1) :    # 이진수 만드는 함수
    a = n // 2
    b = n % 2
    tmp1 += str(b)
    if a == 0 : return str(tmp1)
    else : return binaryNum(a, tmp1)
    
def solution(s):
    answer = []
    cnt1 = 1
    cnt2 = 0
    tmp1 = ''
    if s == 1 : return [0,0]
    a = s
    if '0' in s :
        cnt2 += s.count('0')
        a = s.replace('0', '')
    while len(a) > 1 :
        tmp2 = binaryNum(len(a), tmp1)
        cnt1 += 1
        cnt2 += tmp2.count('0')
        a = tmp2[::-1].replace('0', '')
    answer.append(cnt1)
    answer.append(cnt2)
    return answer