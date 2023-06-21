def solution(n):
    a = list(map(str, str(n)))
    a.sort(reverse = True)
    return int("".join(a))