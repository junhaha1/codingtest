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
      red = (i, j)
    if board[i][j] == 'B':
      blue = (i, j)

dir = [(0, -1), (1, 0), (0, 1), (-1, 0)] #up = 0, right = 1, down = 2, left = 3
q = deque()

#초기 큐 삽입
info = (red, blue, 0, 0) #레드 위치, 블루 위치, 방향, 횟수
q.append(info)

while q: #큐가 빌 때까지 조사
  pass