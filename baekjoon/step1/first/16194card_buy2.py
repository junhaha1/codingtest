from sys import stdin

input = stdin.readline

n = int(input())

p = [0] + list(map(int, input().rstrip().split()))

dp = [0] * (n + 1)
dp[1] = p[1]

for i in range(2, n + 1):
    dp[i] = p[i]
    for j in range(1, i + 1):
        dp[i] = min(dp[i], dp[i-j] + p[j])
print(dp[n])