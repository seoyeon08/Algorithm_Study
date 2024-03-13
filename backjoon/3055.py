import collections
R, C = map(int, input().split())
maps = [list(input().strip()) for _ in range(R)]        # 지도
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]                   # 위치를 저장
count = [[0] * C for _ in range(R)]

queue = collections.deque()                             # 움직인 queue

def BFS(x, y) :
    
    return "KAKTUS"