from sys import stdin
from collections import deque

input = stdin.readline

u, v  = map(int, input().rstrip().split())

board = [[] for _ in range(u + 1)]
for _ in range(v):
  i, j = map(int, input().rstrip().split())
  board[i].append(j)
  board[j].append(i)


dist = [0] * (u + 1)
cnt = 0

def graph(s, cnt):
  q = deque()
  dist[s] = cnt
  q.append(s)
  while q:
    s = q.popleft()
    for i in range(len(board[s])):
      if dist[board[s][i]] == 0: #아직 방문하지 않았다면
        dist[board[s][i]] = cnt
        q.append(board[s][i])

for i in range(1, len(dist)):
  if dist[i] == 0:
    cnt += 1
    graph(i, cnt)

print(cnt)
    