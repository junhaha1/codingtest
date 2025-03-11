from sys import stdin

input = stdin.readline
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
dp[3] = 4

nums = []
for _ in range(int(input())):
  nums.append(int(input().rstrip()))
  
for i in range(4, max(nums)+1):
  dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009
  
for i in nums:
  print(dp[i])