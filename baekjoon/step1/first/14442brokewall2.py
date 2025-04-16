from sys import stdin
from collections import deque

input = stdin.readline

n,m,k = map(int, input().split())

visited = [[[0] * m for _ in range(n)] for _ in range(k + 1)]
board = [list(map(int, input().rstrip())) for _ in range(n)]

def bfs(k, r, c):
  dis = [(-1,0), (1, 0), (0, -1), (0, 1)]
  
  q = deque()
  q.append((k, r, c))
  visited[k][r][c] = 1
  
  while q:
    k, r, c = q.popleft()
    
    if r == n - 1 and c == m - 1: #갈 수 있을 경우 종료
      return visited[k][r][c]
    
    for d in dis:
      nr = r + d[0]
      nc = c + d[1]
      
      if 0<= nr < n and 0 <= nc < m:
        if board[nr][nc] == 0 and visited[k][nr][nc] == 0: #벽을 부수지 않을때
          visited[k][nr][nc] = visited[k][r][c] + 1
          q.append((k, nr, nc))
        if k > 0 and board[nr][nc] == 1 and visited[k-1][nr][nc] == 0: #벽을 부쉈을 때
          visited[k-1][nr][nc] = visited[k][r][c] + 1
          q.append((k-1, nr, nc))
  return -1

print(bfs(k, 0, 0))