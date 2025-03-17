from sys import stdin
from collections import deque

input = stdin.readline

n = int(input().rstrip())

board = [list(input().rstrip()) for _ in range(n)]

nums = 0 #단지 수
result = [] #단지 내 집 수

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(y,x):
  count = 0
  queue = deque()
  
  board[y][x] = '0'
  count += 1
  
  queue.append((y, x))
  
  while queue:
    y, x = queue.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      
      if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == '1':
        board[ny][nx] = '0'
        count += 1
        queue.append((ny,nx))
  return count

for i in range(n):
  for j in range(n):
    if board[i][j] == '1':
      nums += 1
      result.append(bfs(i,j))
      
result.sort()
print(nums, *result, sep='\n')