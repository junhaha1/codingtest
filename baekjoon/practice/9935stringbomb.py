from sys import stdin

input = stdin.readline
string = input().rstrip()
bomb = input().rstrip()

stack = []

for s in string:
    stack.append(s)
    if ''.join(stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))