def solution(array, commands):
    answer = []

    for i in commands:
        a = array[i[0]-1 : i[1]]  # i[0]은 자르기 시작하는 숫자가 위치, i[1]은 어디까지 자를지
        a.sort()  # 정렬
        answer.append(a[i[2]-1])
        
    return answer