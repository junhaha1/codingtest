from sys import stdin
from collections import deque
from itertools import permutations

input = stdin.readline

dm = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(start, end):
  visited = [[0] * w for _ in range(h)]
  q = deque()
  visited[start[0]][start[1]] = 1
  q.append((start[0], start[1]))
  
  while q:
    x, y = q.popleft()
    if x == end[0] and y == end[1]:
      return visited[x][y] - 1
    for i in dm:
      nx = x + i[0]
      ny = y + i[1]
      if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and board[nx][ny] != 'x':
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx, ny))
  return -1

while True:
  w, h = map(int, input().rstrip().split())
  if w+h:
    board = [list(input().rstrip()) for _ in range(h)]
  else:
    break
  
  check = False
  #청소기 위치
  robot_loc = ()
  #청소 위치
  clean_loc = []

  for i in range(h):
    for j in range(w):
      if board[i][j] == 'o':
        robot_loc = (i,j)
      elif board[i][j] == '*':
        clean_loc.append((i,j))
    
  robot_start_loc = []
  for end in clean_loc:
    dis = bfs(robot_loc, end)
    if dis == -1: check = True
    robot_start_loc.append(dis)
  
  if check:
    print(-1)
    continue
  
  dists = [[0] * len(clean_loc) for _ in range(len(clean_loc))]

  for i in range(len(clean_loc)):
    for j in range(len(clean_loc)):
      if clean_loc[i] != clean_loc[j]:
        dis = bfs(clean_loc[i], clean_loc[j])
        dists[i][j], dists[j][i] = dis, dis
  
  result = int(10e9)
  for per in permutations(range(len(clean_loc))):
    temp = robot_start_loc[per[0]]
    start = per[0]
    for end in per[1:]:
      temp += dists[start][end]
      start = end
    result = min(temp, result)
  
  print(result)