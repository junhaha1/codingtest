from sys import stdin 
import heapq

input = stdin.readline

n, k = map(int, input().rstrip().split())
obj = [[0,0]]

for _ in range(n):
  obj.append(list(map(int, input().rstrip().split())))


bags = [[0] * (k + 1) for _ in range(n + 1)] #각 무게에 대한 최댓값

for i in range(1, n + 1):
  for j in range(1, k + 1):
    w = obj[i][0] #무게
    v = obj[i][1] #비용 
    
    if j < w: #넣을 수 없으므로 이전 거 가져오기
      obj[i][j] = obj[i-1][j]
    else:
      pass
      