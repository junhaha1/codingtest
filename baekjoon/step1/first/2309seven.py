from itertools import combinations
from sys import stdin

input = stdin.readline

m = [int(input()) for _ in range(9)]

c = list(combinations(m, 7))

result = None
for t in c:
  if sum(t) == 100:
    result = list(t)
    break
result.sort()
for s in result:
  print(s)