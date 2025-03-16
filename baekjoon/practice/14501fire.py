from sys import stdin

input = stdin.readline

n = int(input().rstrip())
t = []
p = []

dp = [0] * (n + 1)

for _ in range(n):
    i, j = map(int, input().rstrip().split())
    t.append(i)
    p.append(j)

t = [0] + t[::-1]
p = [0] + p[::-1]
d = n
for i in range(1, n + 1):
    if d + t[i] > n + 1: 
        dp[i] = dp[i-1]
    else:
        dp[i] = max(dp[i-1], dp[i-t[i]] + p[i])
    d -= 1
print(dp[-1])
