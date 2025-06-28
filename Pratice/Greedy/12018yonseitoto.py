from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
cnt = 0
temp = []
for i in range(n):
    h, c = map(int, input().split())
    l_m = list(map(int, input().split()))
    
    if m > 0:
        if c > h:
            cnt += 1
            m -= 1
        else:
            l_m.sort(reverse=True)
            temp.append(l_m[c-1])

temp.sort()
for t in temp:
    if m >= t:
        cnt += 1
        m -= t
    else:
        break
print(cnt)