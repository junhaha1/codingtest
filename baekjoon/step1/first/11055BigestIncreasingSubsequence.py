from sys import stdin

input = stdin.readline

n = int(input().rstrip())

seq = list(map(int, input().rstrip().split()))

dp = [0] * n
dp[0] = seq[0]

for i in range(1, n):
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j] + seq[i])
        else:
            dp[i] = max(dp[i], seq[i])

print(max(dp))