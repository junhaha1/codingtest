from sys import stdin
from collections import deque

input = stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    dag = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    dp = [0] * (N + 1)

    for _ in range(K):
        X, Y = map(int, input().split())
        dag[X].append(Y)
        in_degree[Y] += 1

    W = int(input())

    q = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            dp[i] = cost[i]
            q.append(i)

    while q:
        cur = q.popleft()
        for next in dag[cur]:
            in_degree[next] -= 1
            dp[next] = max(dp[next], dp[cur] + cost[next])
            if in_degree[next] == 0:
                q.append(next)

    print(dp[W])
