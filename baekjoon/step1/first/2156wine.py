from sys import stdin

input = stdin.readline

n = int(input().rstrip())

wine = [0]
for _ in range(n):
  wine.append(int(input().rstrip()))
  
dp = [0] * (n + 1)
dp[1] = wine[1]

if n > 1:
  dp[2] = wine[1] + wine[2]

if n > 2:
  dp[3] = max(wine[3] + wine[2], dp[2], wine[3]+ wine[1])
  
for i in range(4, n + 1):
  dp[i] = max(dp[i-1], wine[i] + dp[i-2], wine[i] + wine[i-1] + dp[i-3])


print(dp[n])