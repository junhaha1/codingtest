from sys import stdin

input = stdin.readline

n = int(input().rstrip())
A = list(map(int, input().rstrip().split()))


#1. 1차원 DP배열을 이용하여 각 인덱스 수로 끝나는 감소 수열에서 수의 갯수 세기
dp = [0] * 1002
for a in A:
  dp[a] = max(dp[a+1:]) + 1
print(max(dp))


#2. 이분탐색을 감소한다는 특징에 맞게 수정하여 작성한 코드
def bs(a, lis): 
  start = 0
  end = len(lis) - 1
  while start <= end:
    mid = (start + end) // 2
    if a >= lis[mid]:
      end = mid - 1
    else:
      start = mid + 1
  return start
      
dp = [A[0]]
for i in range(1, n):
  if A[i] < dp[-1]:
    dp.append(A[i])
  elif A[i] > dp[-1]:
    idx = bs(A[i], dp)
    dp[idx] = A[i]

print(len(dp))