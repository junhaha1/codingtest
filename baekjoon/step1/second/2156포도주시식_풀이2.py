N = int(input())

wine = []
for _ in range(N):
    wine.append(int(input()))

dp = [[0] * N for _ in range(3)]

if N == 1:
    print(wine[0])
    exit(0)
if N == 2:
    print(wine[0] + wine[1])
    exit(0)

dp[0][0] = 0
dp[1][0] = wine[0]
dp[2][0] = 0

dp[0][1] = wine[0]
dp[1][1] = wine[1]
dp[2][1] = wine[0] + wine[1]

for i in range(2, N):
    dp[0][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])
    dp[1][i] = dp[0][i-1] + wine[i]
    dp[2][i] = dp[1][i-1] + wine[i]

print(max(dp[0][N-1], dp[1][N-1], dp[2][N-1]))