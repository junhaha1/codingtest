from sys import stdin

input = stdin.readline

n = int(input())

dp = [0] * 101

dp[1] = 9

for i in range(2, n + 1):
  dp[i] = (dp[i-1] * 2) -1
  
print(dp[n])
  