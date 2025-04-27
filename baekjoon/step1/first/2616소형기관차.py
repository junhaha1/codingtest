from sys import stdin

input = stdin.readline

N = int(input())
train = list(map(int, input().split()))
prev_sum = [0]

K = int(input())

for t in train:
    prev_sum.append(prev_sum[-1] + t)

dp = [[0] * (N + 1) for _ in range(4)]

for i in range(1, 4):
    for j in range(K, N + 1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-K] + (prev_sum[j] - prev_sum[j - K]))

print(dp[-1][-1])
