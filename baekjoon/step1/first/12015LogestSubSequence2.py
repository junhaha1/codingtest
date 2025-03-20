from sys import stdin

input = stdin.readline

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))

dp = [a[0]]

def bs(lis, num):
  s = 0
  e = len(lis) -1
  while s <= e:
    m = (s + e) // 2
    if lis[m] < num:
      s = m + 1
    elif lis[m] >= num:
      e = m - 1
  return s

for i in range(1, n):
  if dp[-1] < a[i]:
    dp.append(a[i])
  else:
    idx = bs(dp, a[i])
    dp[idx] = a[i]
    
print(len(dp))