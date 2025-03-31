from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().rstrip().split())

board = [list(map(int, input().rstrip().split())) for _ in range(n)]

dm = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def bfs(x, y):
  q = deque()
  q.append((x,y))
  while q:
    x, y = q.popleft()
    for d in dm:
      nx = x + d[0]
      ny = y + d[1]
      if 0 <= nx < n and 0 <= ny < m:
        if board[nx][ny] == 0:
          board[nx][ny] = board[x][y] + 1
          q.append((nx, ny))
        else:
          if board[nx][ny] > board[x][y] + 1:
            board[nx][ny] = board[x][y] + 1
            q.append((nx, ny))
            
 # print(board)
for i in range(n):
  for j in range(m):
    if board[i][j] == 1:
      bfs(i, j)

dis = 0
for i in range(n):
  for j in range(m):
    dis = max(dis, board[i][j])
print(dis-1)