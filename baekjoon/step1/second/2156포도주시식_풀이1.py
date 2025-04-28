from sys import stdin

input = stdin.readline

N = int(input())

wine = []
for _ in range(N):
    wine.append(int(input()))

if N == 1:
    print(wine[0])
    exit(0)
if N == 2:
    print(wine[0] + wine[1])
    exit(0)
if N == 3:
    print(max(wine[1] + wine[2], wine[0] + wine[1], wine[0] + wine[2])) #연속으로 먹기, 현재꺼 안먹기, 앞앞 + 현재꺼
    exit(0)

dp = [0] * N
dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(wine[1] + wine[2], wine[0] + wine[1], wine[0] + wine[2])

for i in range(3, N):
    dp[i] = max(dp[i-3] + wine[i-1] + wine[i], dp[i-1], dp[i-2] + wine[i])

print(dp[N-1])