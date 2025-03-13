from sys import stdin
input = stdin.readline

def count(lis):
  ans = 1
  for i in range(len(lis)):
    cnt = 1
    for j in range(1, len(lis[i])):
      if lis[i][j-1] == lis[i][j]:
        cnt += 1
      else:
        cnt = 1
      ans = max(ans, cnt)
      
    cnt = 1
    for j in range(1, len(lis[i])):
      if lis[j-1][i] == lis[j][i]:
        cnt += 1
      else:
        cnt = 1
      ans = max(ans, cnt)  
  return ans

def solve(lis):
  cnt = -1
  for i in range(n):
    for j in range(1, n):
      #오른쪽과 바꾸기
      lis[i][j], lis[i][j-1] = lis[i][j-1], lis[i][j]
      cnt = max(cnt, count(lis))
      lis[i][j-1], lis[i][j] = lis[i][j], lis[i][j-1]
      
      #아래와 바꾸기
      lis[j][i], lis[j-1][i] = lis[j-1][i], lis[j][i]
      cnt = max(cnt, count(lis))
      lis[j-1][i], lis[j][i] = lis[j][i], lis[j-1][i]
  return cnt

n = int(input())
cn = [list(input().rstrip()) for _ in range(n)]
#cn_t = list(map(list,zip(*cn))) #전치 행렬 변환

print(solve(cn))