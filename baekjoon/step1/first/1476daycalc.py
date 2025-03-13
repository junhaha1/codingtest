from sys import stdin

input = stdin.readline
e, s, m = map(int, input().rstrip().split())

se, ss, sm = [1, 1, 1]
y = 1
while True:
  if e == se and s == ss and m == sm:
    break
  
  se += 1
  ss += 1
  sm += 1
  
  if se == 16: se = 1
  if ss == 29: ss = 1
  if sm == 20: sm = 1

  y += 1
print(y)
  