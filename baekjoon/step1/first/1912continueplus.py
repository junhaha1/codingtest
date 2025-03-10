from sys import stdin

input = stdin.readline

n = int(input().rstrip())

nums = list(map(int, input().rstrip().split()))
dp = [0] * n
dp[0] = nums[0]
for i in range(1, n):
  dp[i] = max(nums[i], dp[i-1] + nums[i])

print(max(dp))
