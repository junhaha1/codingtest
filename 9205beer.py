#9205번 맥주 마시면서 걸어가기

from collections import deque
from math import ceil
t = int(input()) #테스트 케이스 갯수

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visit_number):
    queue = deque()
    queue.append((x, y))
    board[x][y] = 1
    market = markets.popleft()
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < fy and 0 <= ny < fx:
                if board[nx][ny] == 0 and (nx != market[1] or ny != market[0]):
                    board[nx][ny] = board[x][y] + 1
                    queue.append((nx, ny))
                if nx == market[1] and ny == market[0]:
                    board[nx][ny] = 0
                    queue.append((nx, ny))

for i in range(t):
    beer = 20 #맥주
    empty_beer = 0 #다 먹은 맥주
    n = int(input()) #편의점 갯수
    
    hx, hy = map(int, input().split()) #집 좌표
    markets = deque()
    for j in range(n): #편의점 좌표 추가
        markets.append(tuple(map(int, input().split())))
    fx, fy = map(int, input().split())
    
    board = [[0 for _ in range(fx)] for _ in range(fy)]
    
    min_beer = ceil((fx + fy) / 50)
    visit_number = ceil(min_beer / 20) -1 #편의점 방문 해야하는 최소 횟수
    
    bfs(hx, hy, visit_number)
    
    print(board[fy-1][fx - 1])
    
    
