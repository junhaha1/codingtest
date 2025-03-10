from sys import stdin

input = stdin.readline

n = int(input().rstrip())

nums = list(map(int, input().rstrip().split()))

for i in range(n - 1):
  print(f"{i}: {nums[i]}, {i+1}: {nums[i+1]}, {nums}")
  if nums[i] < nums[i + 1]:
    nums[i] = max(nums[i] + nums[i+1], nums[i-1] + nums[i+1])

print(nums)