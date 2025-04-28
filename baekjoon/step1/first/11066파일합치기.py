from sys import stdin

input = stdin.readline

for _ in range(int(input())):
  K = int(input())
  files = list(map(int, input().rstrip().split()))
  prev_sum = [0]

  #구간합 구해두기
  for i in range(len(files)):
    prev_sum.append(prev_sum[-1] + files[i])
  
  dp = [[0] * K for _ in range(K)]
  for length in range(2, K + 1):
    for i in range(K - length + 1): #해당 구간 시작하는 인덱스
      j = i + length - 1 #해당 구간이 끝나는 인덱스
      dp[i][j] = int(1e9)
      for panel in range(i, j):
        dp[i][j] = min(dp[i][j], dp[i][panel] + dp[panel + 1][j] + prev_sum[j + 1] - prev_sum[i])
  
  print(dp[0][-1])