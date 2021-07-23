a, b = map(int, input().split()) # a, b를 각각 입력받는다

# 역순으로 저장하기
a = int(a[::-1]) 
b = int(b[::-1]) 

print(a) if a > b else print(b)
