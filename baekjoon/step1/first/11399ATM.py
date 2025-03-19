from sys import stdin

input = stdin.readline
n = int(input())
m = list(map(int, input().rstrip().split()))

m.sort()
t = [m[0]]

for i in range(1, n):
  t.append(t[-1] + m[i])
  
print(sum(t))