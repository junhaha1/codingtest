from sys import stdin

input = stdin.readline

def ucl(a, b):
  while r := a % b:
    a = b
    b = r
  
  return b

n = int(input().rstrip())
for _ in range(n):
  nums = list(map(int, input().rstrip().split()))
  t = nums[0]
  nums = nums[1::]
  result = 0
  for i in range(t):
    for j in range(i + 1, t):
      result += ucl(nums[i], nums[j])

  print(result)
  