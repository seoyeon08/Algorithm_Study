def solution(a, b):
    li = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    last = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = -1
    month = a - 1
    for i in range(month) :
        count += last[i]
    return li[(count + b) % 7]