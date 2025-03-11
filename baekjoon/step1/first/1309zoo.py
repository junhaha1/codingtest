from sys import stdin

input = stdin.readline

n = int(input().rstrip())

dp = [[0,0,0,0] for _ in range(n + 1)]

dp[1] = [0, 1, 1, 1]
#           ox, xo, xx
for i in range(2, n + 1):
  dp[i][1] = (dp[i-1][3] + dp[i-1][2]) % 9901
  dp[i][2] = (dp[i-1][1] + dp[i-1][3]) % 9901
  dp[i][3] = sum(dp[i-1]) % 9901 #dp[i-1][1] + dp[i-1][2] + dp[i-1][3]
  
print(sum(dp[-1]) % 9901)