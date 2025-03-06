from sys import stdin

input = stdin.readline

b = int(input())

t = [0, 1, 2] + [0] * 998

if not (b == 1 or b == 2):
  for i in range(3, b + 1):
    t[i] = (t[i-1] + t[i-2]) % 10007
  
print(t[b])