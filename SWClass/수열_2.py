from sys import stdin

input = stdin.readline

n, k = map(int, input().split())

t = list(map(int, input().split()))

result = [sum(t[:k])]

for i in range(1, n- k + 1):
  result.append(result[-1] - t[i-1] + t[i + k - 1])
  
print(max(result))