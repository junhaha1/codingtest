from sys import stdin

input = stdin.readline

nums = []

for _ in range(int(input())):
  nums.append(int(input()))
  
n = max(nums)
dp = [[0,0,0,0] for _ in range(n+1)]
dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]
for i in range(4, n + 1):
  dp[i][1] = (dp[i-1][2] + dp[i-1][3]) %1000000009
  dp[i][2] = (dp[i-2][1] + dp[i-2][3]) %1000000009
  dp[i][3] = (dp[i-3][1] + dp[i-3][2]) %1000000009
  
for n in nums:
  print(sum(dp[n])%1000000009)
  