from sys import stdin
from collections import deque

input = stdin.readline
N, M = map(int, input().split())
board = []
for _ in range(N):
  board.append(list(input().rstrip()))

red = (0, 0)
blue = (0, 0)
for i in range(N):
  for j in range(M):
    if board[i][j] == 'R':
      red = [i, j]
      board[i][j] = '.'
    if board[i][j] == 'B':
      blue = [i, j]
      board[i][j] = '.'


def move(x, y, dx, dy):
  count = 0
  while board[y + dy][x + dx] != '#' and board[y][x] != 'O':
    y += dy
    x += dx
    count += 1
  return y, x, count


dir = [(0, -1), (1, 0), (0, 1), (-1, 0)] #up = 0, right = 1, down = 2, left = 3
q = deque()

#초기 큐 삽입
info = (red[0], red[1], blue[0], blue[1], 0) #레드 위치, 블루 위치, 횟수
q.append(info)

visited = set()

while q:
  ry, rx, by, bx, depth = q.popleft()
  if depth >= 10:
    break
  for d in dir:
    nry, nrx, r_count = move(rx, ry, d[0], d[1])
    nby, nbx, b_count = move(bx, by, d[0], d[1])

    if (nrx, nry) == (rx, ry) and (nbx, nby) == (bx, by):
      continue 

    if board[nby][nbx] == 'O':
      continue

    if board[nry][nrx] == 'O':
      print(depth + 1)
      exit()
    
    if (nry, nrx) == (nby, nbx):
      if r_count > b_count:
        nry -= d[1]
        nrx -= d[0]
      else:
        nby -= d[1]
        nbx -= d[0]
      
    if (nry, nrx, nby, nbx) not in visited:
      visited.add((nry, nrx, nby, nbx))
      q.append((nry, nrx, nby, nbx, depth + 1))

print(-1)