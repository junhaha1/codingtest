from sys import stdin, maxsize

input = stdin.readline

n = int(input())

rgb = [list(map(int, input().rstrip().split() ))for _ in range(n)]

ans = maxsize
for i in range(3):
    dp = [[1001] * 3 for _ in range(n)]
    dp[0][i] = rgb[0][i]
    for j in range(1, n):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + rgb[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + rgb[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + rgb[j][2]
    dp[-1][i] = maxsize
    ans = min(ans, min(dp[-1]))
print(ans)
    

