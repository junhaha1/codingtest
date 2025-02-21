from sys import stdin

input = stdin.readline

n, l = map(int, input().split())

m = []
for _ in range(n):
    m.append(list(map(int, input().split())))
    
m.sort(key=lambda x: x[0])

tree = m[0][0]
total_count = 0
for start, end in m:
    if tree > end: #나무의 위치가 웅덩이 끝보다 크다면
        continue
    elif tree < start:
        tree = start
    dist = end - tree
    remainder = 1
    if dist % l == 0:
        remainder = 0
    count = dist // l + remainder
    tree += count * l
    total_count += count
print(total_count)
