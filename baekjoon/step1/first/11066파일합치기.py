from sys import stdin
import heapq

input = stdin.readline

for _ in range(int(input())):
  K = int(input())
  files = list(map(int, input().rstrip().split()))
  heapq.heapify(files)
  
  result = 0
  while len(files) != 1:
    a = heapq.heappop(files)
    b = heapq.heappop(files)
    heapq.heappush(files, a+b)
    result += (a + b)
  print(result)
  