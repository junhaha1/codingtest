from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    N = int(input())
    st = [list(map(int, input().rstrip().split())) for _ in range(2)]

    if N == 1:
        print(max(st[0][0], st[1][0]))
        continue
    dp = [[0] * (N + 1) for _ in range(2)]
    dp[0][1] = st[0][0]
    dp[1][1] = st[1][0]
    result = -1
    for j in range(2, N + 1):
        dp[0][j] = max(dp[1][j-1], dp[0][j-2], dp[1][j-2]) + st[0][j-1]
        dp[1][j] = max(dp[0][j-1], dp[0][j-2], dp[1][j-2]) + st[1][j-1]

        result = max(dp[0][j], dp[1][j])
    print(result)
