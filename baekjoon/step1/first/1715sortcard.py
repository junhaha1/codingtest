from sys import stdin
import heapq

input = stdin.readline
n = int(input())
heap = []

for _ in range(n):
  heapq.heappush(heap, int(input()))

result = 0
while len(heap) != 1:
  temp = heapq.heappop(heap) + heapq.heappop(heap)
  result += temp
  heapq.heappush(heap, temp)

print(result)
