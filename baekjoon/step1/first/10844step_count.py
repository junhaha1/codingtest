from sys import stdin

input = stdin.readline

n = int(input())

dp = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(101)]
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n + 1):
  for j in range(10):
    if j == 0:
      dp[i][0] = dp[i-1][1] % 1000000000
    if j == 9:
      dp[i][9] = dp[i-1][8] % 1000000000
    if 1 <= j <=8:
      dp[i][j] += dp[i-1][j - 1] % 1000000000
      dp[i][j] += dp[i-1][j + 1] % 1000000000
    

print(sum(dp[n]) % 1000000000)