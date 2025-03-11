from sys import stdin

input = stdin.readline

n ,k = map(int, input().rstrip().split())

dp = [[1 for _ in range(n + 1)] for _ in range(k)]

for i in range(1, k):
  for j in range(1, n + 1):
     dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000

print(dp[k-1][n])