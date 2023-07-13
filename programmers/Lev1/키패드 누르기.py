def solution(numbers, hand):
    answer = ''
    checkL, checkR = 10, 12
    for i in numbers :
        if i == 0 : i = 11
        # 왼손
        if i == 1 or i == 4 or i == 7 : 
            answer += "L"
            checkL = i
        # 오른손
        elif i == 3 or i == 6 or i == 9 : 
            answer += "R"
            checkR = i
        # 2, 5, 8일때, 가까운거 판단하기
        else :
            if (abs(i - checkR) == 3 and abs(i - checkL) ==1) or (abs(i - checkL) == 3) and abs(i -checkR) == 1 :
                if hand == "left" : answer += "L"
                else : answer += "R"
            elif abs(checkL-i) > abs(checkR-i) :
                checkR = i
                answer += "R"
            elif abs(checkL-i) < abs(checkR-i) : 
                checkL = i
                answer += "L"   
            
    return answer