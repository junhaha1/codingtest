from sys import stdin
input = stdin.readline

n = int(input())
nums = list(map(int, input().rstrip().split()))
dp1 = [0] * n
dp2 = [0] * n

dp1[0] = nums[0]
dp2[0] = nums[0]
for i in range(1, n):
    dp1[i] = max(dp1[i-1] + nums[i], nums[i])
    dp2[i] = max(dp2[i-1] + nums[i], dp1[i-1])
print(max(max(dp1),max(dp2)))