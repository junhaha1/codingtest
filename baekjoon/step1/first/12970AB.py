from sys import stdin

input = stdin.readline

n, k = map(int, input().rstrip().split())

dp = ['B'] * n
cnt = 0

def solve(n, k, cnt):
  for i in range(n//2 + 1):
    cnt = max(cnt, i * (n - i))
  if cnt < k:
    print(-1)
    return
  
  cnt = 0
  while cnt != k:
    cnt -= dp.count('A')
    idx = n - 1
    dp[idx] = 'A'
    
    while idx > 0 and dp[idx-1] == 'B' and cnt != k:
      dp[idx] = 'B'
      idx -= 1
      dp[idx] = 'A'
      cnt += 1
  
  print(''.join(dp))
  return 

solve(n,k,cnt)
      