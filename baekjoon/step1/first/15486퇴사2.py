from sys import stdin

input = stdin.readline

N = int(input())

dp = [0] * (N + 1)

for i in range(1, N + 1):
    day, value = map(int, input().split())
    if i + day - 1 <= N:
        dp[i + day - 1] = max(dp[i-1] + value, dp[i + day - 1])
    dp[i] = max(dp[i-1], dp[i])

print(dp[N])