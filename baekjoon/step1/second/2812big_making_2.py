from sys import stdin

input = stdin.readline

n, k = map(int, input().rstrip().split())
num = list(map(int, input().rstrip()))
stack = []
cnt = 0
for nu in num:
    while stack and stack[-1] < nu and cnt < k:
        stack.pop()
        cnt += 1
    
    stack.append(nu)

if cnt < k:
    stack = stack[:-(k-cnt)]
# for i in stack:
#     print(i, end='')

print(''.join(map(str,stack)))