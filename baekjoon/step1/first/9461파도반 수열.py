from sys import stdin

input = stdin.readline
for _ in range(int(input())):
  N = int(input())
  if N <= 3:
    print(1)
    continue
  dp = [0] * N
  dp[0] = dp[1] = dp[2] = 1
  
  for i in range(3, N):
    dp[i] = dp[i-3] + dp[i-2]
  
  print(dp[N-1])