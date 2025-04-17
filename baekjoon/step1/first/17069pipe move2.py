from sys import stdin

input = stdin.readline

n = int(input())

board = []
for _ in range(n):
  board.append(list(map(int, input().split())))
  
  
dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1

for i in range(n):
  for j in range(1, n):
    if i == 0 and j == 1: continue
    if board[i][j] == 0:
      dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1] 
      dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
      if board[i-1][j] == 0 and board[i][j-1] == 0:
        dp[2][i][j] = dp[2][i-1][j-1] + dp[0][i-1][j-1] + dp[1][i-1][j-1]
          
      
# for i in range(3):
#   print()
#   print(*dp[i], sep='\n')
print(dp[0][n-1][n-1] + dp[1][n-1][n-1] + dp[2][n-1][n-1])