from sys import stdin
from collections import deque
from itertools import combinations
input = stdin.readline

def BFS(virus, board, zero):
    visited = [[False] * N for _ in range(N)]
    q = deque()
    for pos in virus:
        y, x = pos
        q.append((y, x, 0))
    max_second = 0
    while q:
        y, x, s = q.popleft()
        for d in dir:
            ny = y + d[0]
            nx = x + d[1]
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] != '-' and visited[ny][nx] == False:
                q.append((ny, nx, s + 1))
                visited[ny][nx] = True
                
                if board[ny][nx] != '*':
                    max_second = max(max_second, s + 1)
                    zero -= 1

    return max_second if zero == 0 else -1
    

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

virus = []
safe = 0 #안전지대 갯수
second = int(1e9)
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append((i, j))
            board[i][j] = '*' #비활성화 바이러스
        elif board[i][j] == 1:
            board[i][j] = '-' #벽
        elif board[i][j] == 0:
            board[i][j] = '.' #안전지대
            safe += 1

if safe == 0:
    print(0)
    exit()

for v in combinations(virus, M):
    result = BFS(v, board, safe)
    if result != -1:
        second = min(second, result)

print(second if second != int(1e9) else -1)