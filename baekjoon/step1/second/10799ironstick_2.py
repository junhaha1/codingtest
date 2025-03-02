from sys import stdin

input = stdin.readline

st = list(input().rstrip())
stack = []
cnt = 0

pre = ''
for s in st:
    if stack:
        if s == ')' and pre == ')':
            cnt += 1
            stack.pop()
        elif s == ')' and stack[-1] == '(':
            stack.pop()
            cnt += len(stack)
        elif s != ')':
            stack.append(s)
    else: #스택이 비었을 때
        stack.append(s)
    pre = s

print(cnt)