from sys import stdin

input = stdin.readline

n = int(input().strip())

dp = [int(input())]
for i in range(1, n):
    line = list(map(int, input().rstrip().split()))
    temp = []
    if i == 1:
        temp.append(line[0] + dp[0])
        temp.append(line[-1] + dp[-1])
    else:
        temp.append(line[0] + dp[0])
        for i in range(1, len(line)-1):
            temp.append(max(dp[i-1] + line[i], dp[i] + line[i]))
        temp.append(line[-1] + dp[-1])
    dp = temp.copy()

print(max(dp))