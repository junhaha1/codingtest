#silver5
from sys import stdin
input = stdin.readline

a, b = map(int, input().rstrip().split())

n = int(input())

nums = list(map(int, input().rstrip().split()))[::-1]

#10진수로 변환하기
result = 0
for i in range(n):
  result += (a ** i) * nums[i]
  
r = []
#주어진 b진법으로 전환하기
while result >= b:
  r.append(result % b)
  result //= b

r.append(result)

print(*r[::-1])