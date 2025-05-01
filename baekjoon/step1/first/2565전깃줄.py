from sys import stdin

input = stdin.readline

N = int(input())

adj = [0] * 501
dp = [0] * 501

for _ in range(N):
    st, ed = map(int, input().rstrip().split())
    adj[st] = ed
    dp[st] = 1

for i in range(1, 501):
    for j in range(1, i):
        if adj[i] > adj[j]:
            dp[i] = max(dp[j] + 1, dp[i])


print(N - max(dp))