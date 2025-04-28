from sys import stdin

input = stdin.readline

adj = []
N = int(input())
for _ in range(N):
    adj.append(list(map(int, input().rstrip().split())))


dp = [[0] * N for _ in range(N)]
for length in range(2, N + 1): # 구간 길이
    for i in range(N - length + 1): #구간 시작점
        j = i + length - 1 #구간 끝점
        dp[i][j] = int(1e9)
        for k in range(i, j): #나누는 지점
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + (adj[i][0] * adj[k][1] * adj[j][1]))

print(dp[0][-1])