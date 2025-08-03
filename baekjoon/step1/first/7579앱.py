import sys

input = sys.stdin.readline

N, M = map(int, input().split())
memorys = list(map(int, input().split()))
costs = list(map(int, input().split()))

total_cost = sum(costs)
dp = [0] * (total_cost + 1)

for i in range(N):
    memory = memorys[i]
    cost = costs[i]
    for j in range(total_cost, cost - 1, -1):
        dp[j] = max(dp[j], dp[j - cost] + memory)
    
for i in range(len(dp)):
    if dp[i] >= M:
        print(i)
        break