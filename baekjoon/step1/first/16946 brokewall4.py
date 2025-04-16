from sys import stdin
from collections import deque

input = stdin.readline
n, m = map(int, input().split())

board = [list(map(int, input().rstrip())) for _ in range(n)]

def bfs(r, c):
    temp = [[0] * m for _ in range(n)]
    dis = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((r, c))
    cnt = 1
    temp[r][c] = 1

    while q:
        r, c = q.popleft()
        for d in dis:
            nr = r + d[0]
            nc = c + d[1]

            if 0<= nr < n and 0 <= nc < m and board[nr][nc] == 0 and temp[nr][nc] == 0:
                temp[nr][nc] = 1
                cnt += 1
                q.append((nr, nc))
    return cnt

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            board[i][j] = bfs(i, j)

for i in range(n):
    print(*board[i], sep='')        

