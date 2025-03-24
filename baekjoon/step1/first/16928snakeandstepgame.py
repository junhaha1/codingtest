from sys import stdin
from collections import deque

input = stdin.readline

n, m  = map(int, input().rstrip().split())

ladder = {}
snake = {}

for _ in range(n):
  a, b = map(int, input().rstrip().split())
  ladder[a] = b

for _ in range(m):
  a, b = map(int, input().rstrip().split())
  snake[a] = b

board = [0] * 101

def bfs(s):
  q = deque()
  q.append(s)
  
  while q:
    x = q.popleft()
    for i in range(1, 7):
      next_x = x + i

      if next_x <= 100 and board[next_x] == 0:

        if next_x in ladder.keys():
          next_x = ladder[next_x]

        elif next_x in snake.keys():
          next_x = snake[next_x]

        if board[next_x] == 0:
          board[next_x] = board[x] + 1
          q.append(next_x)

bfs(1)
print(board[-1])