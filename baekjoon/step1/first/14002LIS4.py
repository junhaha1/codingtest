from sys import stdin

input = stdin.readline

n = int(input())
a = [0] + list(map(int, input().rstrip().split()))

dp = [0] + [1] * n

for i in range(2, n + 1):
  for j in range(1, i):
    if a[i] > a[j]:
      dp[i] = max(dp[i], dp[j] + 1)

max_count = max(dp)
print(max_count)
lis = []
i = n

while max_count > 0:
  if dp[i] == max_count:
    lis.append(a[i])
    max_count -= 1
  i -= 1
  
print(*lis[::-1])