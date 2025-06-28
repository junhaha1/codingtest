from sys import stdin
#중간값으로 판단하기
input = stdin.readline

n = int(input())

maps = []
result = []
m = 0

for _ in range(n):
    x, a = map(int, input().split())
    maps.append((x, a))
    m += a

maps.sort(key=lambda x : x[0])
m = int((m+1)/2)
temp = 0
for x, a in maps:
    temp += a
    if temp >= m:
        print(x)
        break

