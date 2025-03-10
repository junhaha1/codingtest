from sys import stdin

input = stdin.readline
n = int(input())
a = [0] + list(map(int, input().split()))

dp = [1] * (n + 1)

#1. DP를 이용 
for i in range(1, n+1):
  for j in range(1, i):
    if a[i] > a[j]:
      dp[i] = max(dp[i], dp[j] + 1)

print(dp[1:])
print(max(dp))


#2. 이분 탐색을 이용
def bin_search(a, lis):
  start = 0
  end = len(lis) - 1
  while start < end:
    mid = (start + end) // 2
    if lis[mid] == a or lis[mid-1] < a < lis[mid]:
      return mid
    elif lis[mid] > a:
      end = mid - 1
    elif lis[mid] < a:
      start = mid + 1
  return start

lis = [a[1]]

for i in range(2, n + 1):
  if lis[-1] < a[i]:
    lis.append(a[i])
  else:
    idx = bin_search(a[i], lis)
    lis[idx] = a[i]
    
print(len(lis))