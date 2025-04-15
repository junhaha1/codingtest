from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
blocksum = [0]
for num in nums:
  blocksum.append(blocksum[-1] + num)
  
for _ in range(m):
  s, e = map(int, input().split())
  
  print(blocksum[e] - blocksum[s-1])