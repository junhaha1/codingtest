from sys import stdin

input = stdin.readline

word1 = [0] + list(input().rstrip())
word2 = [0] + list(input().rstrip())

row = len(word2)
col = len(word1)

dp = [[0] * row for _ in range(col)]

#LCS 알고리즘
for i in range(1, col):
    for j in range(1, row):
        if word1[i] == word2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

#LCS 역추적 알고리즘
if dp[-1][-1] == 0:
    exit(0)
result = []
i = col - 1
j = row - 1
while dp[i][j] != 0:
    if word1[i] == word2[j]:
        result.append(word1[i])
        i -= 1
        j -= 1
    else:
        if dp[i][j-1] > dp[i-1][j]:
            j -= 1  
        else:
            i -= 1
            
result.reverse()
print(''.join(result))