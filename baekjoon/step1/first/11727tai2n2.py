from sys import stdin

input = stdin.readline

n = int(input())

t = [0] * 1001
t[1] = 1
t[2] = 3

for i in range(1, n - 1):
  t[i+2] = (t[i+1] + (t[i] * 2)) % 10007

print(t[n])