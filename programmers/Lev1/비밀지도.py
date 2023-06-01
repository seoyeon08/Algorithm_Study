def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2) :       # arr1, arr2를 한번에 i,j로 for 돌기
        a = str(bin(i|j)[2:].zfill(n))  # i, j를 이진수 변환 및 or 계산해서 문자열 형태로 a에 담기
        a = a.replace('1', '#')         # 1은 #으로 교체
        a = a.replace('0', ' ')         # 0은 공백으로 교체
        answer.append(a)                # answer에 a 담기
    return answer