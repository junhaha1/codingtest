from sys import stdin
from collections import deque

input = stdin.readline

n, m  = map(int, input().rstrip().split())

steps = [tuple(map(int, input().rstrip().split())) for _ in range(n)]
steps = sorted(steps, key=lambda x : x[0])
snakes = [tuple(map(int, input().rstrip().split())) for _ in range(m)]
snakes = sorted(snakes, key=lambda x : x[0])

board = [int(1e9) for _ in range(101)]

def bfs(s):
  q = deque()
  q.append(s)
  board[s] = 0
  
  while q:
    pre_idx = q.popleft()
    cur_idx = pre_idx
    
    for _ in range(6):
      cur_idx += 1
      if cur_idx <= 100: #이동한 좌표가 100보다 작거나 같으면
        check = True
        for st in steps:
          if cur_idx == st[0] and board[pre_idx] + 1< board[st[1]]:
            board[cur_idx] = board[pre_idx] + 1
            board[st[1]] = board[cur_idx]
            q.append(st[1])
            check = False
            break
        for sn in snakes:
          if cur_idx == sn[0] and board[pre_idx] + 1 < board[sn[1]]:
            board[cur_idx] = board[pre_idx] + 1
            board[sn[1]] = board[cur_idx]
            q.append(sn[1])
            check = False
            break
          
        if check and board[cur_idx] > board[pre_idx] + 1:
          board[cur_idx] = board[pre_idx] + 1
          q.append(cur_idx)
bfs(1)
print(board[-1])