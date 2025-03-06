from sys import stdin
input = stdin.readline

def find_123(a):
  global cnt
  if a > 0:
    find_123(a - 1)
    find_123(a - 2)
    find_123(a - 3)
  if a == 0:
    cnt += 1
    
for _ in range(int(input())):
  cnt = 0
  find_123(int(input()))
  print(cnt)