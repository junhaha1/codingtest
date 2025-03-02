from sys import stdin

input = stdin.readline

n = int(input())
count = 1
stack = []
op = []
fail = False

for _ in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1
    
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        fail = True
        break
    
if fail:
    print('NO')
else:
    for o in op:
        print(o)