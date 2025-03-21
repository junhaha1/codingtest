from sys import stdin

input = stdin.readline

def toggle(l, i, n):
  for j in [i-1, i, i + 1]:
    if 0 <= j < n:
      l[j] = 1 - l[j]
    

def solve(n, light1, target):
  light2 = light[:]
  MAX = int(1e9)
  #1. 1번 전구를 누르지 않았을 경우
  count1 = 0
  for i in range(1, n):
    if light1[i-1] != target[i-1]:
      toggle(light1, i, n)
      count1 += 1
      
  if light1 != target:
    count1 = MAX
    
  count2 = 1
  toggle(light2, 0, n)
  for i in range(1, n):
    if light2[i-1] != target[i-1]:
      toggle(light2, i, n)
      count2 += 1
      
  if light2 != target:
    count2 = MAX
    
  result = min(count1, count2)
  print(result if result != MAX else -1)
  
n = int(input())
light = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))
solve(n, light, target)
