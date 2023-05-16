n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]
    count = 0
    for score in nums[1:]:
        if score > avg:
            count += 1  # 평균 이상의 학생 수
    rate = count/nums[0] *100
    print(f'{rate:.3f}%')