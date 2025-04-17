from sys import stdin

input = stdin.readline

n = int(input())
board = []
for _ in range(n):
  board.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
# 0번 가로, 1번 세로, 2번 대각선

#가로 파이프 초기화
dp[0][1] = 1

d = [(0,0,1)] #파이프 번호, 좌표
dis = [(0, 1), (1, 0), (1, 1)] #갈 수 있는 방향 (가로, 세로, 대각선)

while d:
  num, x, y = d.pop()
  for i in range(len(dis)):
    if num == 0 and i == 1: continue #가로인 경우 가로, 대각선만 가능
    if num == 1 and i == 0: continue #세로인 경우 세로, 대각선만 가능
    
    new_num = i #방향
    nx = x + dis[i][0]
    ny = y + dis[i][1]
    if 0<= nx < n and 0 <= ny < n and board[nx][ny] == 0:
      if new_num == 2 and (board[x+1][y] == 1 or board[x][y+1] == 1):
        continue
      dp[nx][ny] += 1
      d.append((new_num, nx, ny))
      
#print(*dp, sep='\n')

print(dp[n-1][n-1])
  
  