from sys import stdin

input = stdin.readline

n, b = input().rstrip().split()
n = n[::-1]
result = 0
for i in range(len(n)):
  if ord(n[i]) >= 65:
    result += (ord(n[i]) - 55) * (int(b) ** i)
  else:
    result += int(n[i]) * (int(b) ** i)
print(result)