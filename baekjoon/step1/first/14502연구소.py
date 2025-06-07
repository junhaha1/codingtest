from sys import stdin
from collections import deque
from copy import deepcopy

input = stdin.readline

def dfs(board, walls, num):
    global result
    if walls == 3:
        count = bfs(board)
        result = max(result, count)
        return
    
    if num < N * M:
        y = num // M
        x = num % M
        dfs(deepcopy(board), walls, num + 1)
        if board[y][x] == 0:
            board[y][x] = 1
            dfs(deepcopy(board), walls + 1, num + 1)

def bfs(board):
    global safe
    temp = safe - 3

    q = deque()
    for v in virus:
        q.append(v)

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dir[i][0]
            nx = x + dir[i][1]
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 0:
                temp -= 1
                board[ny][nx] = 2
                q.append((ny, nx))
    
    return temp

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

virus = []
safe = 0
result = 0
rem = set()

for y in range(N):
    for x in range(M):
        if board[y][x] == 2:
            virus.append((y, x))
        elif board[y][x] == 0:
            safe += 1
            
dfs(board, 0, 0)
print(result)