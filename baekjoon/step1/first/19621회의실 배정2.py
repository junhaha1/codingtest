N = int(input())

board = [tuple(map(int, input().split())) for _ in range(N)]
board.sort()

dp = [[0] * N for _ in range(2)]

for i in range(2):
    for j in range(i, N):
        if i == j:
            dp[i][j] = board[j][2]
        elif j - 2< 0:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i][j-2] + board[j][2])

print(max(dp[0][-1], dp[1][-1]))