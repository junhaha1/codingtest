from sys import stdin

input = stdin.readline

n, s = map(int, input().rstrip().split())

def gcd(a, b):
  while r := a % b:
    a = b
    b = r
  return b

nums = [abs(i - s) for i in list(map(int, input().rstrip().split()))]

temp = nums[0]

for i in range(1, n):
  temp = gcd(temp, nums[i])
  
print(temp)
  