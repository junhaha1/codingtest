N = int(input())


board = [[0] * (N) for _ in range(N)]
queens = [-1] * N

def check(r, c):
  for row, col in enumerate(queens):
    if row == r or col == -1:
      continue
    if abs(r - row) == abs(c - col) or c == col: #대각선에 위치하거나 같은 열에 있다면
      return False
  return True

def dfs(row, col):
  if col < 0 or col == N or row == N or -1 not in queens:
    return
  
  dfs()
  
for i in range(N):
  dfs(0, i)
  