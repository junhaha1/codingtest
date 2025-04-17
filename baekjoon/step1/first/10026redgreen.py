from sys import stdin
from collections import deque

input = stdin.readline
n = int(input())
board = []

for _ in range(n):
  board.append(list(input().rstrip()))
  
result = [[0] * n for _ in range(n)]
dis = [(1,0),(-1,0),(0,-1),(0,1)]

def bfs(number, r, c):
  q = deque()
  q.append((r, c))
  result[r][c] = number
  visited[r][c] = True
  
  while q:
    r, c = q.popleft()
    for d in dis:
      nr = r + d[0]
      nc = c + d[1]
      if 0<= nr < n and 0 <= nc < n and visited[nr][nc] == False and board[r][c] == board[nr][nc]:
        result[nr][nc] = number
        visited[nr][nc] = True
        q.append((nr, nc))

visited = [[False] * n for _ in range(n)]  
number = 0

for i in range(n):
  for j in range(n):
    if visited[i][j] == False:
      bfs(number, i, j)
      number += 1

for i in range(n):
  for j in range(n):
    if board[i][j] == "G":
      board[i][j] = "R"
      
      
visited = [[False] * n for _ in range(n)]  
number2 = 0
for i in range(n):
  for j in range(n):
    if visited[i][j] == False:
      bfs(number2, i, j)
      number2 += 1
      
#print(*result, sep='\n')
print(number, number2)
  