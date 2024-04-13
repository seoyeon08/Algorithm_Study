n = int(input())
balloon = list(map(int, input().split()))
idx = 0
answer = []
li = [i for i in range(1, n + 1)]
tmp = balloon.pop()
answer.append(li.pop(idx))

for _ in range(n) :
    if tmp > 0 :
        idx = (idx + tmp - 1) % n
    else :
        idx = (idx + tmp) % n
    tmp = balloon.pop(idx)
    answer.append(li.pop(idx))
print(answer)