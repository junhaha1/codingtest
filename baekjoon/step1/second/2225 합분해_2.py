from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
MOD = 1000000000

dp = [[1] + ([0] * N) for _ in range(K + 1)]

for i in range(1, K + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(dp[K][N] % MOD)