from sys import stdin
from collections import deque

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
shark_pos = None
time = 0
shark_size = 2
shark_eat = 0

direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]

for i in range(N):
  for j in range(N):
    if board[i][j] == 9:
       shark_pos = (i, j)
       board[i][j] = 0
       
       
def bfs(shark_pos, shark_size):
  fishs = []
  distance = [[-1] * N for _ in range(N)]
  q = deque()
  q.append(shark_pos)
  distance[shark_pos[0]][shark_pos[1]] += 1
  
  while q:
    y, x = q.popleft()
    for d in direction:
      ny = y + d[0]
      nx = x + d[1]
      if 0 <= ny < N and 0 <= nx < N and distance[ny][nx] == -1:
        if board[ny][nx] <= shark_size:
          distance[ny][nx] = distance[y][x] + 1
          q.append((ny, nx))
          if 0 < board[ny][nx] < shark_size:
            fishs.append((distance[ny][nx], ny, nx))
  return sorted(fishs)

while True:
  fishs = bfs(shark_pos, shark_size)
  
  if not fishs:
    break
  
  dist, ny, nx = fishs[0]
  shark_eat += 1
  board[ny][nx] = 0
  shark_pos = (ny, nx)
  time += dist
  
  if shark_eat == shark_size:
    shark_size += 1
    shark_eat = 0
  
print(time)