from sys import stdin
from sys import maxsize
input = stdin.readline

n, m = map(int, input().split())

meats = []
result = []
for _ in range(n):
    x, a = map(int, input().split())
    meats.append((x, a))
    
meats.sort(key=lambda x : (x[1], -x[0]))

ans = maxsize
weight, same = 0, 0
check = False
for i in range(n):
    weight += meats[i][0]
    if i >= 1 and meats[i][1] == meats[i-1][1]:
        same += meats[i][1]
    else:
        same = 0
    if weight >= m:
        ans = min(ans, meats[i][1] + same)
        check = True
    
print(ans if check else -1)    