#9205번 맥주 마시면서 걸어가기

from collections import deque
from math import ceil
t = int(input()) #테스트 케이스 갯수

def bfs():
    queue = deque()
    queue.append((hx, hy))

    while queue:
        x, y = queue.popleft()
        if abs(fx - x) + abs(fy - y) <= 1000:
            print('happy')
            return 
        for i in range(n):
            if visited[i] == 0:
                new_x, new_y = markets[i]
                if abs(x - new_x) + abs(y - new_y) <= 1000:
                    visited[i] = 1
                    queue.append((new_x, new_y))

    print('sad')
    return 


for i in range(t):
    beer = 20 #맥주
    empty_beer = 0 #다 먹은 맥주
    n = int(input()) #편의점 갯수
    
    hx, hy = map(int, input().split()) #집 좌표
    markets = []
    for j in range(n): #편의점 좌표 추가
        markets.append(tuple(map(int, input().split())))
    fx, fy = map(int, input().split())
    
    visited = [0 for _ in range(n)]
    
    bfs()
