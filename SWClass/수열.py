from sys import stdin

input = stdin.readline

n, k = map(int, input().split())

t = list(map(int, input().split()))

temp = [t[0]]

for i in range(1, n):
  temp.append(temp[-1] + t[i])
  
result = temp[k-1]
  
for i in range(k, n):
  result = max(result, temp[i] - temp[i - k])
  
print(result)