from sys import stdin
from collections import deque

input = stdin.readline
N = 16
result = []
dis = [(1,0), (-1,0), (0, -1), (0, 1)]

def bfs(r, c):
  q = deque()
  q.append((r, c))
  
  while q:
    r, c = q.popleft()
    if board[r][c] == 3:
      return 1
    
    for d in dis:
      nr = r + d[0]
      nc = c + d[1]
      
      if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != 1 and board[nr][nc] != -1:
        if board[nr][nc] != 3:
          board[nr][nc] = -1
        q.append((nr, nc))
  return 0
    
  
  
for _ in range(10): 
  num = int(input())
  board = [list(map(int, input().rstrip())) for _ in range(N)]
  r = bfs(1,1)
  
  result.append((num, r))

for res in result:
  print('#' + str(res[0]) + " " + str(res[1]))