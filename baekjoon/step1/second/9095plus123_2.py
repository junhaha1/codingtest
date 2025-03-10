from sys import stdin

input = stdin.readline

t = int(input())
#1. dp테이블을 1차원 배열로 만들어 점화식을 직접 구현
dp = [0] * 12

dp[1] = 1
dp[2] = 2
dp[3] = 4
for _ in range(t):
  n = int(input())
  for i in range(4, n + 1):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    
  print(dp[n])
  
#2. dp테이블을 2차원 배열로 만들어 끝나는 수에 따라 다르게 구현
dp = [[0, 0, 0, 0] for _ in range(12)]

dp[1] = [0, 1, 0, 0]
dp[2] = [0, 1, 1, 0]
dp[3] = [0, 2, 1, 1]

t = int(input())

for _ in range(t):
  n = int(input())
  for i in range(4, n + 1):
    dp[i][1] = dp[i-1][1] + dp[i-1][2] + dp[i-1][3]
    dp[i][2] = dp[i-2][1] + dp[i-2][2] + dp[i-2][3]
    dp[i][3] = dp[i-3][1] + dp[i-3][2] + dp[i-3][3]
  print(sum(dp[n]))
