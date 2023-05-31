def solution(n):
    answer = []
    ans = 0
    while n :
        ans = n % 10
        answer.append(ans)
        n //= 10
    return answer