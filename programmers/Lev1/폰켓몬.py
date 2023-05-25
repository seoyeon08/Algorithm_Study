def solution(nums):
    answer = 0
    a = list()
    for i in nums :
        if len(a) < len(nums)//2 :
            if i not in a :
                a.append(i)
                answer += 1
        else : break
    return answer