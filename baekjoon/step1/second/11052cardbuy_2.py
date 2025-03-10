from sys import stdin

input = stdin.readline

n = int(input())
card = [0] + list(map(int, input().rstrip().split()))

dp = [0] * (n + 1)

dp[1] = card[1]
for i in range(2, n + 1):
  for j in range(1, i + 1):
    dp[i] = max(dp[i], dp[i-j] + card[j])
    
print(dp[n])
# dp[1] = card[1]
# for i in range(2, n + 1):
#   dp[i] = card[i]
#   max_price = 0
#   for j in range(i // 2 + 1):
#     if (price := dp[i-j] + card[j]) > max_price:
#       max_price = price
#   dp[i] = max_price

print(dp[n])