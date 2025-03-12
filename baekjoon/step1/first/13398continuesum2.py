n = int(input())
nums = list(map(int, input().rstrip().split()))

dp = [[0] * n for _ in range(2)]

dp[0][0] = nums[0] #기존 연속합 더하기
dp[1][0] = nums[0] #연속합2를 구하기

result = 0
for i in range(1, n):
  dp[0][i] = max(nums[i], dp[0][i-1] + nums[i])
  dp[1][i] = max(dp[1][i-1]  + nums[i] , dp[0][i-1])
  result = max(result, dp[0][i], dp[1][i])
print(max(max(dp[0]), max(dp[1])))