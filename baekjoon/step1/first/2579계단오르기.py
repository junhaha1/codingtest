from sys import stdin

input = stdin.readline

N = int(input())
dp = [0] * N

step = []

for _ in range(N):
    step.append(int(input()))

if N == 1:
    print(step[0])
    exit(0)
if N == 2:
    print(step[0] + step[1])
    exit(0)


dp[0] = step[0]
dp[1] = step[0] + step[1]
dp[2] = max(dp[0] + step[2], step[1] + step[2])

for i in range(3, N):
    dp[i] = max(dp[i-3] + step[i-1], dp[i-2]) + step[i]

print(dp[-1])