from sys import stdin
input = stdin.readline

def gcd(x, y):
  while y:
    x, y = y, x % y
  return x

#핵심
#n과 m으로 나머지 연산을 했을 경우 x, y가 나오는 공통값을 찾는 문제
for _ in range(int(input())):
  n, m, x, y = map(int, input().rstrip().split())
  max_y = n * m // gcd(n, m)
  
  while True:
    if x > max_y:
      print(-1)
      break
    if (x - y) % m == 0:
      print(x)
      break
    x += n
    
    
