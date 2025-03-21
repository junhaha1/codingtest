from sys import stdin

input = stdin.readline

n = int(input())
d = [0] * (n + 1) #메모이제이션 사용하기

#1부터 n까지 올라가면서 구하기
for i in range(2, n+1): #bottom-up 방식
  d[i] = d[i-1] + 1
  if i % 2 == 0:
    d[i] = min(d[i], d[i//2] + 1)
  if i % 3 == 0:
    d[i] = min(d[i], d[i//3] + 1)

print(d[n])