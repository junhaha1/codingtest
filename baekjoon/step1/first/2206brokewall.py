from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split()) # 세로 가로 

board = [list(map(int, input().rstrip())) for _ in range(n)]

visited = [[[0] * m for _ in range(n)] for _ in range(2)]

dis = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(r, c):
  q = deque()
  q.append((1, r, c))
  visited[1][r][c] = 1
  
  while q:
    t, r, c = q.popleft()
    if r == n - 1 and c == m - 1:
      return visited[t][r][c]
    
    for d in dis:
      nr = r + d[0]
      nc = c + d[1]
      
      if 0 <= nr < n and 0 <= nc < m:
        if board[nr][nc] == 0 and visited[t][nr][nc] == 0: #벽이 아니라면
          visited[t][nr][nc] = visited[t][r][c] + 1
          q.append((t, nr, nc))
        if t > 0 and board[nr][nc] == 1 and visited[t-1][nr][nc] == 0: #벽이 이라면
          visited[t-1][nr][nc] = visited[t][r][c] + 1
          q.append((t-1, nr, nc))
          
  return -1
  
print(bfs(0,0))