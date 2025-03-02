from sys import stdin

input = stdin.readline
left = list(input().rstrip())
right = []
m = int(input())

for _ in range(m):
    w = input().rstrip()
    if w == 'L' and len(left) > 0:
        right.append(left.pop())
    elif w == 'D' and len(right) > 0:
        left.append(right.pop())
    elif w == 'B' and len(left) > 0:
        left.pop()
    elif 'P' in w:
        w, c = w.split()
        left.append(c)
        

print(''.join(left + right[::-1]))
