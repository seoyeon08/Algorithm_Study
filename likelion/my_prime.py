arr = []
def is_prime(num):
    if num < 2 :              # 2 이하는 소수가 아니다
        return False
    if num in (2,3):
        return True
    if num % 2 == 0 or num % 3 == 0 :   # 2나 3으로 나누어지면 소수가 아니다
        return False
    for i in range(2, num) :
        if num % i == 0 :   # 주어진 숫자들 중에서 서로 나눴을 때 나눠지면 소수가 아니다
            return False
        else:
            return True         # 아무것도 나누어지지 않으면 소수이다

    # 들어온 num이 소수이면 True를 반환하고
    # 소수가 아니면 False를 반환하는 함수
    

def calculate_prime_number(length):
    for i in range(2, length + 10) :    # 범위를 지정해주기..
        while len(arr) < length :       
            if is_prime(i) == True:     # 소수이면 배열에 추가하기
                arr.append(i)
            i += 1
        return arr



n = int(input('Length? '))
print(calculate_prime_number(n))