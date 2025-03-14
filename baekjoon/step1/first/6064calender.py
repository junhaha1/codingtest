from sys import stdin

input = stdin.readline

for _ in range(int(input())):
  n, m, x, y = map(int, input().rstrip().split())
  year = x
  while True:
    if (year - x) % n ==0 and (year - y) % m == 0:
      print(year)
      break
    
    year += n
    
    if year > n*m:
      print(-1)
      break