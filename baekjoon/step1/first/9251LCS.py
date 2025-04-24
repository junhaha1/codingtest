from sys import stdin
input = stdin.readline

str1 = [0] + list(input().rstrip())
str2 = [0] + list(input().rstrip())
row = len(str2)
col = len(str1)

#print(str1, str2)

dp = [[0] * col for _ in range(row)]

for i in range(1, row):
    for j in range(1, col):
        if str2[i] == str1[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[row-1][col-1])