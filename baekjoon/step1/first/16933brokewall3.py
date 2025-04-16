from sys import stdin
from collections import deque

input = stdin.readline

n, m, k = map(int, input().rstrip().split())

visited = [[[0] * m for _ in range(n)] for _ in range(k + 1)]
board = [list(map(int, input().rstrip())) for _ in range(n)]

def bfs(k, r, c):
  dis = [(-1,0), (1,0), (0,-1), (0,1)]
  q = deque()
  q.append((1, k, r, c, True)) 
  visited[k][r][c] = 1
  
  while q:
    dist, k, r, c, day = q.popleft() #True 낮, False 밤
    
    if r == n - 1 and c == m - 1:
      return dist
    
    for d in dis:
      nr = r + d[0]
      nc = c + d[1]
      
      if 0 <= nr < n and 0 <= nc < m:
        if board[nr][nc] == 0 and visited[k][nr][nc] == 0:
          visited[k][nr][nc] = dist + 1
          q.append((dist + 1, k, nr, nc, not day))
        if k > 0 and board[nr][nc] == 1 and visited[k-1][nr][nc] == 0:
          if day: #낮인 경우 바로 이동
            visited[k-1][nr][nc] = dist + 1
            q.append((dist + 1, k-1, nr, nc, not day))
          else: #밤인 경우 그냥 넣기
            q.append((dist + 1, k, r, c, not day))
  return -1

print(bfs(k, 0, 0))