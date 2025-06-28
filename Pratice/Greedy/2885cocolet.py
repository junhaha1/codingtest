from sys import stdin

input = stdin.readline
k = int(input())

lst = [2**i for i in range(21)]
c = 0

for t in lst:
    if k <= t:
        c = t
        break

cnt = 0
if c != k:
    tmp = c
    while k != 0:
        tmp //= 2
        if k >= tmp:
            k -= tmp
            cnt += 1     
        else:
            cnt += 1
print(c, cnt)
    